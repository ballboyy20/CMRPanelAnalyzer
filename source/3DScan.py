import numpy
import pymesh
from utilities import find_outliers


class Scan:
    def __init__(self, scan_filepath: str):
        self.scan_filepath = scan_filepath
        self.point_array = None
        self.face_list = None
        self.point_group_labels = None
        self.point_outlier_exclusion = None
        # The following are variables meant to be adjustable to the user
        self.outlier_method = 'trev_iter'
        self.group_similarity_ratio_limit = 2.5

    # TODO: Implement this function
    def _kmeans_grouping(self):
        # This will use k-means to identify the groups of points (ignoring those markes 'False' in the
        # point_outlier_exclusion map) and save them to the instance variable point_group_labels
        pass

    # TODO: Implement this function
    def _remove_group_outliers(self):
        # This can only run if point_group_labels has been solved
        """
        for group in labeled_groups:
            find group outliers
            apply outlier map to rows of full outlier map
            update label map to be in reference to non-outlier rows
        """
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
