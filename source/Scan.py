import numpy as np
import pyvista
from source.utilities import *
from source.Visualizer import Visualizer


class Scan:
    def __init__(self, scan_filepath: str, amount_of_clusters: int)-> None:

        self.scan_filepath = scan_filepath
        self.amount_clusters = amount_of_clusters
        self.array_of_3D_points = None
        self.plane_equations = np.zeros((amount_of_clusters, 4)) # this is four becuase an equation for a plane has 4 coefs
        self.face_list = None
        self.cluster_map = None
        self.point_outlier_exclusion = None
        self.scan_visualizer = Visualizer()
        # The following are variables meant to be adjustable to the user
        self.group_similarity_ratio_limit = 2.5

    def extract_3D_data(self) ->None:
            
        mesh_object = pyvista.read(self.scan_filepath)

        self.array_of_3D_points = mesh_object.points
        self.face_list = mesh_object.faces

        self.point_outlier_exclusion = np.ones(self.array_of_3D_points.shape[0],dtype=bool)

    def get_array_of_3D_points(self) -> np.ndarray:
        if self.array_of_3D_points is None:
            raise ValueError("3D data has not been extracted yet. Call extract_3D_data first.")
        return self.array_of_3D_points

    def get_cluster_map(self) -> np.array:
        """Check to see if cluster_map has been created and creates it if it hasn't been created"""
        if self.cluster_map is None:
            self.create_clusters()
        return self.cluster_map
    
    def create_clusters(self) ->None:
        '''creates a np.arrays that contain points that are clustered together'''

        self.cluster_map = identify_clusters_Kmeans(self.array_of_3D_points,self.amount_clusters)
        
        pass

    def remove_outliers_from_each_cluster(self):
        ''' Creates a boolean masks that say which points are outliers (false) and which are inliers (true)'''
        
        self.point_outlier_exclusion = np.ones(self.array_of_3D_points.shape[0], dtype=bool)
    
        for i in np.unique(self.get_cluster_map()):
            # Mask to select points belonging to the current cluster
            cluster_inlier_mask = (self.cluster_map == i)
            
            # Get the points in the current cluster
            points_in_cluster = self.array_of_3D_points[cluster_inlier_mask]
            
            # Remove outliers using RANSAC for this cluster
            cluster_outlier_mask, plane_equation = remove_outliers_ransac(points_in_cluster, return_plane_equation=True)
            
            # Grab the plane equation output from remove_outliers_ransac and store it to the class attribute
            self.plane_equations[i] = plane_equation
            
            # Update point_outlier_exclusion for the current cluster
            # Only update the relevant indices in point_outlier_exclusion
            self.point_outlier_exclusion[cluster_inlier_mask] = cluster_outlier_mask

        pass

    def get_clusters(self):
        ''' generator function that produces views of each of the ordered clusters of the 3D points '''

        for cluster_label in np.unique(self.cluster_map):
            temp_cluster_mask = (self.cluster_map == cluster_label)
            temp_cluster_inliers = self.point_outlier_exclusion & temp_cluster_mask
            #yield cluster_label, self.array_of_3D_points[temp_cluster_inliers], self.plane_equations[cluster_label]
            yield cluster_label, self.plane_equations

    def get_individual_cluster(self, cluster: int) ->np.array:

        individual_cluster = (self.cluster_map == cluster)
        individual_cluster_inliers = (individual_cluster & self.point_outlier_exclusion)

        return self.array_of_3D_points[individual_cluster_inliers]


    def visualize_clusters(self):
        self.scan_visualizer.scatter_plot_clusters_different_colors(self.get_array_of_3D_points(),self.get_cluster_map())

    def visualize_outliers_and_inliers(self):
        
        # Error handling
        if self.array_of_3D_points is None or self.point_outlier_exclusion is None:
            raise ValueError("Some things need to happen before you can execute this function")
        
        if len(self.array_of_3D_points) != len(self.point_outlier_exclusion):
            raise ValueError("Mismatch between array_of_3D_points and point_outlier_exclusion lengths.")
    
        self.scan_visualizer.plot_outliers_and_inliers_together(
        self.array_of_3D_points[~self.point_outlier_exclusion, :],  # View of outliers
        self.array_of_3D_points[self.point_outlier_exclusion, :])    # View of inliers


    def visualize_clean_clusters(self):
        """This will plot the clusters without the outliers."""
        # Error handling
        if self.array_of_3D_points is None:
            raise ValueError("Some things need to happen before you can execute this function. array_of_3D_points is None")
        if self.point_outlier_exclusion is None:
            raise ValueError("Some things need to happen before you can execute this function. point_outlier_exclusion is None")
        
        # Use views (which are already happening with slicing)
        self.scan_visualizer.scatter_plot_clusters_different_colors(
            self.array_of_3D_points[self.point_outlier_exclusion, :],   # View of inliers
            self.cluster_map[self.point_outlier_exclusion])            # View of inlier map