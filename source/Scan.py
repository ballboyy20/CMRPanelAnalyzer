import numpy as np
import pymesh
from source.utilities import *
from source.Visualizer import Visualizer


class Scan:
    def __init__(self, scan_filepath: str, amount_of_clusters: int)-> None:

        self.scan_filepath = scan_filepath
        self.amount_clusters = amount_of_clusters
        self.array_of_3D_points = None
        self.face_list = None
        self.cluster_map = None
        self.point_outlier_exclusion = None
        self.scan_visualizer = Visualizer()
        # The following are variables meant to be adjustable to the user
        self.group_similarity_ratio_limit = 2.5

    def extract_3D_data(self) ->None:
            
        mesh_object = pymesh.load_mesh(self.scan_filepath)

        self.array_of_3D_points = mesh_object.vertices
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
            cluster_outlier_mask = remove_outliers_ransac(points_in_cluster)
            
            # Update point_outlier_exclusion for the current cluster
            # Only update the relevant indices in point_outlier_exclusion
            self.point_outlier_exclusion[cluster_inlier_mask] = cluster_outlier_mask

        pass

    def get_clusters(self):
        ''' generator function that produces views of each of the ordered clusters of the points'''

        for cluster_label in np.unique(self.cluster_map):
            this_cluster_mask = (self.cluster_map == cluster_label)
            this_cluster_inliers = self.point_outlier_exclusion & this_cluster_mask
            yield cluster_label, self.array_of_3D_points[this_cluster_inliers]
            

    def get_individual_cluster(self, cluster: int) ->np.array:

        individual_cluster = (self.cluster_map == cluster)
        individual_cluster_inliers = (individual_cluster & self.point_outlier_exclusion)

        return self.array_of_3D_points[individual_cluster_inliers]


    def visualize_clusters(self):
        self.scan_visualizer.scatter_plot_clusters_different_colors(self.get_array_of_3D_points(),self.get_cluster_map())

    def visualize_outliers_and_inliers(self):
        
        outliers = self.array_of_3D_points[~self.point_outlier_exclusion, :]
        inliers = self.array_of_3D_points[self.point_outlier_exclusion, :]  

        # Plot the outliers and inliers
        self.scan_visualizer.plot_outliers_and_inliers_together(outliers, inliers)