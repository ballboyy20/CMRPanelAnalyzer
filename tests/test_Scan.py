from source.Scan import *
import matplotlib.pyplot as plt
import numpy as np
from source.Visualizer import Visualizer



def test_get_clusters():
    synthetic_data = create_two_random_planes

    test_scan = TestScan(synthetic_data,amount_of_clusters=2)

    test_scan.create_clusters
    test_vis = Visualizer

    test_vis.scatter_plot_clusters_different_colors(test_scan.array_of_3D_points, test_scan.cluster_map)




class TestScan(Scan):
    def __init__(self, data_array: np.ndarray, amount_of_clusters: int) -> None:
        super().__init__(scan_filepath=None, amount_of_clusters=amount_of_clusters)  # Call the parent constructor
        self.array_of_3D_points = data_array  
  

def create_two_random_planes(total_number_points: int=1000, z_value: int=2, x_y_value_range: int=25, group_value: int=50) -> np.array:

    # this function creates a random panel
    # you give it total amount of points, where you want the z value to be, 
    # and a different value for the range of x,y values 
    # this makes it so you get a plane as opposed to like a cube or sphere or something weird
    # Sorry this function is messy I was trying to go quick

    list_of_random_3D_points = np.zeros((total_number_points,3))
    list_of_random_3D_points2 = np.zeros((total_number_points,3))


    for point in range(total_number_points):
        random_x_value = np.random.uniform(group_value,group_value+x_y_value_range)
        random_y_value = np.random.uniform(group_value,group_value+x_y_value_range)
        random_z_value = np.random.uniform(-z_value,z_value)

        random_point = (random_x_value,random_y_value,random_z_value)
        list_of_random_3D_points[point, :] = random_point

    for point in range(total_number_points):
        random_x_value = np.random.uniform(-group_value,-(group_value+x_y_value_range))
        random_y_value = np.random.uniform(-group_value,-(group_value+x_y_value_range))
        random_z_value = np.random.uniform(-z_value,z_value)

        random_point = (random_x_value,random_y_value,random_z_value)
        list_of_random_3D_points2[point, :] = random_point

    list_of_random_3D_points = np.vstack((list_of_random_3D_points,list_of_random_3D_points2))

    number_of_outliar_points = int(np.ceil(total_number_points*0.01))

    for point in range(number_of_outliar_points):
        random_x_value = np.random.uniform(-group_value,group_value)
        random_y_value = np.random.uniform(-group_value,group_value)
        random_z_value = np.random.uniform(-group_value,group_value)

        outlier_point = (random_x_value,random_y_value,random_z_value)
        list_of_random_3D_points[point, :] = outlier_point

    return list_of_random_3D_points


import pyvista as pv


def plot_clusters(points):
    """Plot the 3D clusters using Matplotlib."""
    # Create a new figure for the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the points in 3D space
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='cyan', s=50, alpha=0.6)

    # Set the title
    ax.set_title('Synthetic 3D Clusters in the Same Plane')

    # Set axes labels
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # Set axis limits (optional, you can customize these)
    ax.set_xlim(min(points[:, 0]), max(points[:, 0]))
    ax.set_ylim(min(points[:, 1]), max(points[:, 1]))
    ax.set_zlim(min(points[:, 2]), max(points[:, 2]))

    # Display the plot
    plt.show()

    
points = create_two_random_planes()
plot_clusters(points)
print(points)
