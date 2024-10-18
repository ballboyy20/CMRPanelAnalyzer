import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Visualizer:
    def __init__(self, font_size: int = 12, font_type: str = 'calibri'):
        self.font_size = font_size
        self.font_type = font_type

    def scatter_plot_clusters_different_colors(self, data: np.array, cluster_map: np.array, cluster_centroids: np.array = None) -> None:
        
        fig, ax = self._create_3d_figure()

        ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=cluster_map, cmap='viridis', marker='o')

        if cluster_centroids is not None:
            for i, centroid in enumerate(cluster_centroids):
                ax.text(centroid[0], centroid[1], centroid[2], f'Cluster {i}', color='black', fontsize=self.font_size)

        self._set_axes_labels(ax, 'Clusters separated by color')
        self._set_view(ax)
        plt.show()

    def plot_outliers_and_inliers_together(self, outlier_points: np.ndarray, inlier_points: np.array, first_color: str='red', second_color: str='blue') -> None:
        
        fig, ax = self._create_3d_figure()

        ax.scatter(outlier_points[:, 0], outlier_points[:, 1], outlier_points[:, 2], c=first_color, s=10, label='Outlier')
        ax.scatter(inlier_points[:, 0], inlier_points[:, 1], inlier_points[:, 2], c=second_color, s=10, label='Inliers')

        self._set_axes_labels(ax)
        self._set_view(ax) 
        plt.legend()
        plt.show()

    def plot_3D_points(self, points: np.array) -> None:
        
        fig, ax = self._create_3d_figure()

        ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='cyan', s=50, alpha=0.6)

        self._set_axes_labels(ax, 'Plot of 3D points')
        self._set_view(ax)
        plt.show()

    def _create_3d_figure(self) -> plt.Figure:
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        return fig, ax

    def _set_axes_labels(self, ax: Axes3D, title: str = None) -> None:
        
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.set_aspect('equal', adjustable='box')

        if title:
            ax.set_title(title)
        # ax.set_xlim([np.min(ax.collections[0]._offsets3d[0]), np.max(ax.collections[0]._offsets3d[0])])
        # ax.set_ylim([np.min(ax.collections[0]._offsets3d[1]), np.max(ax.collections[0]._offsets3d[1])])
        # ax.set_zlim([np.min(ax.collections[0]._offsets3d[2]), np.max(ax.collections[0]._offsets3d[2])])

    def _set_view(self, ax: Axes3D) -> None: 
        # Set view to the x-y plane
        ax.view_init(90,-90,0)
        # use this webstie to adjust this
        # https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html