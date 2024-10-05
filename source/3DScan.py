import numpy as np
import pymesh
from source.utilities import *


class Scan:
    def __init__(self, scan_filepath: str)-> None:
        self.scan_filepath = scan_filepath
        self.point_array = None
        self.face_list = None
        self.point_group_labels = None
        self.point_outlier_exclusion = None
        # The following are variables meant to be adjustable to the user
        self.outlier_method = 'trev_iter'
        self.group_similarity_ratio_limit = 2.5

    # This will use k-means to identify the groups of points (ignoring those marked 'False' in the
    # point_outlier_exclusion map) and save them to the instance variable point_group_labels
    def _kmeans_grouping(self):
        # The user must extract points before calling k-means
        if self.point_array is None:
            raise AttributeError('Extract 3d points from the mesh by calling the "get_3d_data"'
                                 'method on this Scan object before attempting to create k-means groups')
        # If no outliers have been indicated this point, all points are assigned as inliers
        if self.point_outlier_exclusion is None:
            print("No outliers were indicated, all points will now be assigned as inliers.")
            self.point_outlier_exclusion = np.full(self.point_array[0], True)
        
        _group_labels, _centroids, _2d_proj_points = kmeans_clusters(self.point_array[self.point_group_labels])
            
        pass

    # TODO: Implement this function
    def _remove_group_outliers(self):
        # This can only run if point_group_labels has been solved
        
        for group in labeled_groups:
            labeled_group[group] = remove_outliers(labeled_group[group],'ransac')
            # find group outliers
            # apply outlier map to rows of full outlier map
            # update label map to be in reference to non-outlier rows
        
        pass

    def get_3d_data(self) -> None:
        mesh_object = pymesh.load_mesh(self.scan_filepath)
        self.point_array = mesh_object.vertices
        self.face_list = mesh_object.faces
    
    def make_groups(self, k_groups: int) -> None:
        # use k-means to create labels for the groups
        self.point_outlier_exclusion = find_outliers(self.point_array, method=self.outlier_method)
        self._kmeans_grouping()
        self._remove_group_outliers()
