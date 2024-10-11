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


class TestScan(Scan):
    def __init__(self, data_array: np.ndarray, amount_of_clusters: int) -> None:
        super().__init__(scan_filepath=None, amount_of_clusters=amount_of_clusters)  # Call the parent constructor
        self.array_of_3D_points = data_array  
  



