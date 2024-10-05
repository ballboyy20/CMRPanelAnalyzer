from source.Panel import Panel
from source.Array import Array
from source.utilities import *
import numpy as np

from sklearn.cluster import KMeans

print('hello world')

# Example 3D data points (array of [x, y, z] coordinates)
points_3d = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [1.1, 2.1, 3.1],
    [7.0, 8.0, 9.0],
    [4.1, 5.1, 6.1],
])

# Define the number of clusters
kmeans = KMeans(n_clusters=2)

# Fit the model and predict cluster labels in one step
cluster_labels = kmeans.fit_predict(points_3d)

# Print out each point and its corresponding cluster label
for point, label in zip(points_3d, cluster_labels):
    print(f"Point {point} is in cluster {label}")