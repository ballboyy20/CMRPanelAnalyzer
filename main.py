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

sandbox_scan = TestScan(create_random_dataset())

sandbox_scan.create_clusters()
