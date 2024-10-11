from source.Scan import *
from tests.test_utilities import create_two_random_planes
import matplotlib.pyplot as plt
import numpy as np




def test_get_clusters():
    synthetic_data = create_two_random_planes()

    test_scan = TestScan(synthetic_data,amount_of_clusters=2)
    test_scan.remove_outliers_from_each_cluster()
    test_scan.visualize_clusters()
    #pytest.fail('FIXME')

def test_visualize_outliers():
    synthetic_data = create_two_random_planes()

    test_scan = TestScan(synthetic_data,amount_of_clusters=2)
    test_scan.remove_outliers_from_each_cluster()
    test_scan.visualize_outliers_and_inliers()
    # pytest.fail('FIXME')

def test_visualize_outliers():
    synthetic_data = create_two_random_planes()

    test_scan = TestScan(synthetic_data,amount_of_clusters=2)
    test_scan.remove_outliers_from_each_cluster()
    test_scan.visualize_clean_clusters()
    # pytest.fail('FIXME')

def test_see_if_array_is_getting_good_clusters(): 
    synthetic_data = create_two_random_planes(total_number_points=20)

    test_scan = TestScan(synthetic_data,amount_of_clusters=2)
    test_scan.remove_outliers_from_each_cluster()

    for cluster_name, cluster_array in test_scan.get_clusters():
        assert isinstance(cluster_array, np.ndarray), f"Expected np.ndarray, got {type(cluster_array)}"

        assert isinstance(cluster_name, np.int32), f"Expected int, got {type(cluster_name)}"

        assert cluster_array.shape[1] == 3, f"Expected array with 3 columns (for 3D points), got something else"

        assert cluster_array.size > 0



class TestScan(Scan):
    def __init__(self, data_array: np.ndarray, amount_of_clusters: int) -> None:
        super().__init__(scan_filepath=None, amount_of_clusters=amount_of_clusters)  # Call the parent constructor
        self.array_of_3D_points = data_array  
  



