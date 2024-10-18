from source.Panel import Panel
from source.Array import Array
from source.Scan import Scan
from tests.test_utilities import *
from source.Visualizer import *
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print('hello world')

class TestScan(Scan):
    def __init__(self, data_array: np.ndarray, amount_of_clusters: int) -> None:
        super().__init__(scan_filepath=None, amount_of_clusters=amount_of_clusters)  # Call the parent constructor
        self.array_of_3D_points = data_array

list_of_random_points = create_two_random_planes()

file_path = "testmesh2.stl"

sandbox_scan = Scan(file_path,amount_of_clusters=4)
sandbox_scan.extract_3D_data()

my_vis = Visualizer()

#my_vis.plot_3D_points(list_of_random_points)

sandbox_scan.create_clusters()
sandbox_scan.remove_outliers_from_each_cluster()
sandbox_scan.visualize_clusters()
sandbox_scan.visualize_clean_clusters()


sandbox_array = Array()
sandbox_array.add_panels_from_3DScan(sandbox_scan)

angle = sandbox_array.compare_two_panels(1,0)
print(angle)


