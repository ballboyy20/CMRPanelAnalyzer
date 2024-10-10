from source.Visualizer import *
from source.utilities import *
import numpy as np
from tests.test_utilities import create_random_dataset

def test_scatter_plot_clusters_different_colors1():
    # Example 3D coordinates dataset
    data = np.array([
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [8, 8, 8],
        [9, 9, 9],
        [10, 10, 10],
        [25, 30, 35],
        [26, 31, 36]
    ])

    # Define the number of clusters (e.g., 3 clusters)
    n_clusters = 3

    labels = identify_clusters_Kmeans(data,n_clusters)

    my_vis = Visualizer

    my_vis.scatter_plot_clusters_different_colors(data,labels)

    assert 1==1

def test_scatter_plot_clusters_different_colors_with_labels1():
    # Example 3D coordinates dataset
    data = np.array([
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [8, 8, 8],
        [9, 9, 9],
        [10, 10, 10],
        [25, 30, 35],
        [26, 31, 36]
    ])

    # Define the number of clusters (e.g., 3 clusters)
    n_clusters = 3

    labels, centroids = identify_clusters_Kmeans(data,n_clusters, return_centroids=True)

    my_vis = Visualizer

    my_vis.scatter_plot_clusters_different_colors(data,labels,centroids)

    assert 1==1

def test_plot_outliers_and_inliers_together(): # TODO This test is currently subjective. How could we make it objective?
    # Create a random dataset
    points = create_random_dataset(1000, 0.001, 50)
    
    # Get the boolean map for inliers
    inlier_map = remove_outliers_ransac(points)
    
    # Get the actual inlier and outlier points
    inliers = points[inlier_map]
    outliers = points[~inlier_map]

    my_vis = Visualizer
    my_vis.plot_outliers_and_inliers_together(outliers,inliers)

    assert 'It looks good' == "It looks good"