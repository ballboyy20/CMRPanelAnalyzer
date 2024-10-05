import numpy as np
import pymesh
from source.utilities import *


class Scan:
    def __init__(self, scan_filepath: str, amount_of_clusters: int)-> None:

        self.scan_filepath = scan_filepath
        self.amount_clusters = amount_of_clusters
        self.array_of_3D_points = None
        self.dict_of_clusters = None
        self.face_list = None
        self.point_group_labels = None
        self.point_outlier_exclusion = None
        # The following are variables meant to be adjustable to the user
        self.group_similarity_ratio_limit = 2.5

    def extract_3D_data(self) -> None:
            
        mesh_object = pymesh.load_mesh(self.scan_filepath)

        self.array_of_3D_points = mesh_object.vertices
        self.face_list = mesh_object.faces


    def create_clusters(self) ->None:
        # creates a dict of np.arrays that contain points that are clustered together

        cluster_map = identify_clusters_Kmeans(self.array_of_3D_points,self.amount_clusters)
        clustered_3D_points_dict = {}

        for i in range(self.amount_clusters):
            mask = cluster_map == i
            points_in_one_cluster = self.array_of_3D_points[mask]
            clustered_3D_points_dict[i] = points_in_one_cluster

        self.dict_of_clusters = clustered_3D_points_dict
        
        pass

    def remove_outliers_from_each_cluster(self):
        # Creates a dict of boolean masks that say which points are outliers (false) and which are inliers (true)

        outlier_boolean_mask_dict = {}
        
        for i in range(self.amount_clusters):

            temp_bool_mask = remove_outliers_ransac(self.dict_of_clusters[i])
            outlier_boolean_mask_dict[i] = temp_bool_mask

        pass
