import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# we want this module to show
    # the entire array after the outliers have been removed with the clusters different colors
    # plot each panel so that a user can give it a name
 # plot each panel with their respective names labeling them
 # to make sure that our process of naming the panels in an array only once, we may want to plot the middle steps of rearranign the panels to line up with one another  

    # something to graph a plane (panel) with its normal vector sticking out (do as a circle to not mislead the orientation of the panels)
    # something to graph the angles between two panels when comparing only two panels (as they actually are) 
    # something to graph the angles between two panels when comparing only two panels (exaggerated to convey conceptually the angle between panels) 
    # use different colored arcs to show the different euler angles between two panels, we'd have to let the user select a ground panel


class Visualizer:
    def __init__(self):
        self.font_size = 12
        self.font_type = 'calibri'

    def scatter_plot_clusters_different_colors(data: np.array, cluster_mask: np.array) -> None:

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(data[:,0],data[:,1],data[:,2],c=cluster_mask,cmap='viridis',marker='o')

        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_zlabel('Z Coordinate')
        plt.title(f'Clusters seperated by color')

        plt.show()

    def scatter_plot_clusters_different_colors_with_labels(data: np.array, cluster_mask: np.array, cluster_centroids: np.array) -> None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the data points, colored by cluster
        scatter = ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=cluster_mask, cmap='viridis', marker='o')

        # Plot each centroid and label with cluster number
        for i, centroid in enumerate(cluster_centroids):
            ax.text(centroid[0], centroid[1], centroid[2], f'Cluster {i}', color='black', fontsize=12)  # Label centroid

        # Set axis labels and title
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_zlabel('Z Coordinate')
        plt.title('Clusters separated by color')

        plt.show()

    def plot_outliers_and_inliers_together(outlier_points: np.array, inlier_points: np.array, first_color: str='red',  second_color: str='blue') -> None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Unpack x, y, z coordinates for both sets
        ax.scatter(outlier_points[:, 0], outlier_points[:, 1], outlier_points[:, 2], c=first_color, s=10, label='Outlier')
        ax.scatter(inlier_points[:, 0], inlier_points[:, 1], inlier_points[:, 2], c=second_color, s=10, label='Inliers')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')

        plt.legend()
        plt.show()
