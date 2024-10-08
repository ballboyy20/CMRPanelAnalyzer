import numpy as np
import pymesh
from source.utilities import *


class Scan:
    def __init__(self, scan_filepath: str, amount_of_clusters: int)-> None:

        self.scan_filepath = scan_filepath
        self.amount_clusters = amount_of_clusters
        self.array_of_3D_points = None
        self.face_list = None
        self.cluster_map = None
        self.point_outlier_exclusion = None
        # The following are variables meant to be adjustable to the user
        self.group_similarity_ratio_limit = 2.5

    def extract_3D_data(self) ->None:
            
        mesh_object = pymesh.load_mesh(self.scan_filepath)

        self.array_of_3D_points = mesh_object.vertices
        self.face_list = mesh_object.faces

        self.point_outlier_exclusion = np.ones(self.array_of_3D_points.shape[0],dtype=bool)


    def create_clusters(self) ->None:
        # creates a np.arrays that contain points that are clustered together

        self.cluster_map = identify_clusters_Kmeans(self.array_of_3D_points,self.amount_clusters)
        
        pass

    def get_clusters(self):
        # generator function that produces views of each of the ordered clusters of the points

        for i in np.unique(self.cluster_map):
            this_cluster_mask = (self.cluster_map == i)
            this_cluster_inliers = self.point_outlier_exclusion & this_cluster_mask
            yield self.array_of_3D_points[this_cluster_inliers]




    def remove_outliers_from_each_cluster(self):
        # Creates a boolean masks that say which points are outliers (false) and which are inliers (true)

        for i in np.unique(self.cluster_map):

            cluster_inlier_mask = (self.cluster_map == i) & self.point_outlier_exclusion
            cluster_outlier_mask = remove_outliers_ransac(self.array_of_3D_points[cluster_inlier_mask])
            self.point_outlier_exclusion[cluster_inlier_mask] = cluster_outlier_mask
              
        pass

    def get_individual_cluster(self, cluster: int) ->np.array:

        individual_cluster = (self.cluster_map == cluster)
        individual_cluster_inliers = (individual_cluster & self.point_outlier_exclusion)

        return self.array_of_3D_points[individual_cluster_inliers]
