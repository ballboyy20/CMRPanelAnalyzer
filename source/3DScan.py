import numpy as np
import pymesh
from source.utilities import *


class Scan:
    def __init__(self, scan_filepath: str, amount_of_clusters: int)-> None:

        self.scan_filepath = scan_filepath
        self.amount_clusters = amount_of_clusters
        self.array_of_3D_points = None
        self.face_list = None
        self.point_group_labels = None
        self.point_outlier_exclusion = None
        # The following are variables meant to be adjustable to the user
        self.group_similarity_ratio_limit = 2.5

    def get_3d_data(self) -> None:
            
        mesh_object = pymesh.load_mesh(self.scan_filepath)

        self.array_of_3D_points = mesh_object.vertices
        self.face_list = mesh_object.faces

            
    def identify_clusters(self) -> np.array:
        
        cluster_map = identify_clusters_with_Kmeans(self.array_of_3D_points, self.amount_clusters)

        return cluster_map

    

    # TODO: Implement this function
    def _remove_group_outliers(self):
        # This can only run if point_group_labels has been solved
        
        for group in labeled_groups:
            labeled_group[group] = remove_outliers(labeled_group[group],'ransac')
            # find group outliers
            # apply outlier map to rows of full outlier map
            # update label map to be in reference to non-outlier rows
        
        pass

    
    
    def make_groups(self, k_groups: int) -> None:
        # use k-means to create labels for the groups
        self.point_outlier_exclusion = find_outliers(self.array_of_3D_points, method=self.outlier_method)
        self._kmeans_grouping()
        self._remove_group_outliers()
