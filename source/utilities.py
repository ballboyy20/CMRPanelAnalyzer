import numpy as np
from typing import Optional
from source.Panel import Panel
import pyvista as pv
import pyransac3d
import json
import os

def get_angle_between_two_vectors(vector_one, vector_two) -> float:
    dot_product = np.dot(vector_two, vector_one)
    
    value = dot_product/(get_magnitude_of_vector(vector_one) * get_magnitude_of_vector(vector_two))
    print(value)
    angle_in_radians = np.arccos(value)

    angle_in_degrees = np.rad2deg(angle_in_radians)

    return angle_in_degrees

def get_magnitude_of_vector(vector: tuple) -> float:
    magnitude = np.sqrt(np.square(vector[0]) + np.square(vector[1]) + np.square(vector[2]))
    return magnitude

def create_random_panel() -> Panel:
    panel_name = "Random Panel"

    # Generate random normal vector with values between 0 and 10
    normal_vector = (np.random.uniform(0.0, 10.0), 
                     np.random.uniform(0.0, 10.0), 
                     np.random.uniform(0.0, 10.0))
    
    # Generate random centroid with values between 0 and 10
    centroid = (np.random.uniform(0.0, 10.0), 
                np.random.uniform(0.0, 10.0), 
                np.random.uniform(0.0, 10.0))

    random_panel = Panel(panel_name,normal_vector, centroid)

    return random_panel

def write_list_dicts_to_json(list_of_dicts: dict, filename: str) -> None: #NOT TESTED WITH PY TEST
    
    with open(filename, 'w') as json_file:
                json.dump(list_of_dicts, json_file, indent=4)

def get_dict_from_json(json_filename: str, directory: str = None) -> dict: #NOT TESTED WITH PY TEST
    
    # If a directory is provided, join it with the filename to create the full path
    if directory:
        file_path = os.path.join(directory, json_filename)
    else:
        # Default to the current working directory if no directory is provided
        file_path = json_filename

    # Open and load the JSON file from the constructed file path
    with open(file_path, 'r') as json_file:
        data_from_json = json.load(json_file)

    return data_from_json

# TODO: Implement this function
# This function is used by the 3DScan module various times, in various places, on both the point list as a whole and then on the individually grouped points, and this is here as a util
def find_outliers(points: np.array, method: Optional[str] = 'trev_iter') -> np.array:
    # This will take a 2d numpy array of points and use either ransac or Trevor's iterative method to generate a 1d map indicating which rows (representing points) in this collection are to be kept (False for outliers)
    if method == 'trev_iter':
        outlier_exclusion_map = remove_outliers_trev_iter(points)
    elif method == 'ransac':
        outlier_exclusion_map = remove_outliers_ransac(points)
    elif method is None:
        outlier_exclusion_map = np.full(points.shape[0], True)
    else:
        raise NotImplementedError
    
    return outlier_exclusion_map

def remove_outliers(points: np.array, method: Optional[str] = 'ransac') -> np.array:

    if method == 'trev_iter':
        outlier_exclusion_map = remove_outliers_trev_iter(points)
    elif method == 'ransac':
        inliers, outliers, equation_for_plane = remove_outliers_ransac(points)
    
    return inliers, outliers, equation_for_plane

# TODO: Implement this function
def remove_outliers_trev_iter(points: np.array) -> np.array:
    pass

def remove_outliers_ransac(points: np.array) -> np.array:

    # Initialize RANSAC for plane fitting
    plane_ransac = pyransac3d.Plane()

    # Fit a plane to the data points
    equation_for_plane, inliers = plane_ransac.fit(points, thresh=.01, maxIteration=1000)

    # Get the outliers
    outliers = np.setdiff1d(np.arange(points.shape[0]), inliers)

    return inliers, outliers, equation_for_plane




def create_random_dataset(total_number_points: int = 100, z_value_range: int = 10, x_y_value_range: int = 20) -> np.array:

    # this function creates a random plane
    # you give it total amount of points, the ranges of z values, 
    # and a different value for the range of x,y values 
    # this makes it so you get a plane as opposed to like a cube or sphere or something weird
     
    list_of_random_3D_points = np.zeros((total_number_points,3))

    for point in range(total_number_points):
        random_x_value = np.random.uniform(-x_y_value_range,x_y_value_range)
        random_y_value = np.random.uniform(-x_y_value_range,x_y_value_range)
        random_z_value = np.random.uniform(-z_value_range,z_value_range)

        random_point = (random_x_value,random_y_value,random_z_value)
        list_of_random_3D_points[point, :] = random_point

    number_of_outliar_points = int(np.ceil(total_number_points*0.01))

    for point in range(number_of_outliar_points):
        random_x_value = np.random.uniform(-x_y_value_range,x_y_value_range)
        random_y_value = np.random.uniform(-x_y_value_range,x_y_value_range)
        random_z_value = np.random.uniform(-x_y_value_range,x_y_value_range)

        outliar_point = (random_x_value,random_y_value,random_z_value)
        list_of_random_3D_points[point, :] = outliar_point

    return list_of_random_3D_points



def plot_3d_points(points_to_be_plotted: np.array, color: str = 'blue'):

    point_cloud = pv.PolyData(points_to_be_plotted)

    plotter = pv.Plotter()
    plotter.add_points(point_cloud, color=color, point_size=10)
    plotter.show()

def plot_two_sets_3D_points(first_set: np.array, second_set: np.array, first_color: str='red',  second_color: str='blue') -> None:

    first_cloud = pv.PolyData(first_set)
    second_cloud = pv.PolyData(second_set)

    plotter = pv.Plotter()

    plotter.add_points(first_cloud, color=first_color,point_size=10)
    plotter.add_points(second_cloud, color=second_color, point_size=10)

    plotter.show()


# Trevor suggested that we make a conversion function that takes any 
# form of an array and converts it to numpy or something that we choose