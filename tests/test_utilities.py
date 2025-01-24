from source.utilities import *
from source.Visualizer_module import Visualizer
import numpy as np

def test_get_angle_between_two_vectors_1():

    vector_one = (0.0, 0.0, 1.0)
    vector_two = (1.0, 0.0, 0.0)
    result = get_angle_between_two_vectors(vector_one, vector_two)

    assert result == 90.0  

def test_get_angle_between_two_vectors_2():

    vector_three = (5.5, -6.5, 2.0)
    vector_four = (-0.25, 0.64, 0.78)
    result = get_angle_between_two_vectors(vector_three, vector_four)

    assert round(result, 6) == 115.926256  # Rounded comparison for floating-point accuracy

def test_get_magnitude_of_vector_1():

    vector = (5.5, -6.5, 2.0)
    result = get_magnitude_of_vector(vector)

    assert round(result,5) == 8.74643


def test_remove_outliars_ransac1(): # TODO test ransac a lot more. 
    # Create a random dataset
    points = create_random_dataset()

    """the ransac function begins to fail when z > 0.01
    Basically its needs to see a really tight range of z values or else it won't
    recognize the plane as a plane. 
    
    This may be an issue for us"""
    
    # Get the boolean map for inliers
    inlier_map = remove_outliers_ransac(points)
    
    # Get the actual inlier and outlier points
    inliers = points[inlier_map]
    outliers = points[~inlier_map]

    test_vis = Visualizer()
    test_vis.plot_outliers_and_inliers_together(outliers, inliers)

    #pytest.fail('Test me more')

def test_remove_outliars_ransac2(): # TODO test ransac a lot more. 
    # Create a random dataset
    points = create_random_dataset()

    """the ransac function begins to fail when z > 0.01
    Basically its needs to see a really tight range of z values or else it won't
    recognize the plane as a plane. 
    
    This may be an issue for us"""
    
    # Get the boolean map for inliers
    inlier_map, equation_for_plane = remove_outliers_ransac(points, return_plane_equation=True)
    
    assert len(equation_for_plane) == 4, f"Expected 4 points in the plane equation, got something else"
    assert isinstance(equation_for_plane, np.ndarray), f"Plane equation was not a numpy array"

    #pytest.fail('Test me more')

def test_kmeans_clustering():
    # Create a dataset manually
    data = np.array([
        [1.0, 2.0],  # Cluster 1
        [1.5, 1.8],  # Cluster 1
        [5.0, 8.0],  # Cluster 2
        [8.0, 8.0],  # Cluster 2
        [1.0, 0.6],  # Cluster 1
        [9.0, 11.0], # Cluster 2
    ])
    
    n_clusters = 2
    
    # Use the kmeans_clustering function
    labels = identify_clusters_Kmeans(data, n_clusters)

    # Check that the number of unique labels matches the number of clusters
    unique_labels = np.unique(labels)
    
    assert len(unique_labels) == n_clusters, f"Expected {n_clusters} clusters, but got {len(unique_labels)}."
    assert all(label in range(n_clusters) for label in unique_labels), "Labels should be in the range of cluster numbers."

    # Additional check to ensure clustering has some variation
    # Count occurrences of each label in the output
    counts = {label: np.sum(labels == label) for label in unique_labels}
    
    # Check that we have some points assigned to each cluster
    assert all(count > 0 for count in counts.values()), "All clusters should have at least one point assigned."


def test_calc_normal_vector_1(): #TODO test this more in depth

    test_data = create_random_dataset()

    normal_vector, best_fit_plane = calc_normal_vector_and_bestfit_plane(test_data)

    assert len(normal_vector) == 3, f"Expected 3 points in the normal vector, got something else"
    assert isinstance(normal_vector, np.ndarray), f"normal vector was not a numpy array"
    assert normal_vector[0] < 1.0
    assert normal_vector[1] < 1.0
    assert normal_vector[2] < 1.0

def test_calc_bestfit_plane1(): #TODO test this more in depth
    test_data = create_random_dataset()
    normal_vector, best_fit_plane = calc_normal_vector_and_bestfit_plane(test_data)
    assert isinstance(best_fit_plane, np.ndarray), f"It's type was not a np.array"
    assert len(best_fit_plane) == 3


    
def test_calc_centroid_from_points():
    test_data = create_random_dataset()
    centroid = calc_centroid_from_points(test_data)
    assert isinstance(centroid, np.ndarray), f"Exptected an array, it was something else"
    assert len(centroid) == 3



########################################################
####### FUNTIONS USED JUST FOR TESTING STUFF ###########
########################################################

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

def create_random_dataset(total_number_points: int = 200, z_value_range: int = .001, x_y_value_range: int = 20) -> np.array:

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

    number_of_outliar_points = int(np.ceil(total_number_points*0.05))

    for point in range(number_of_outliar_points):
        random_x_value = np.random.uniform(-x_y_value_range,x_y_value_range)
        random_y_value = np.random.uniform(-x_y_value_range,x_y_value_range)
        random_z_value = np.random.uniform(-x_y_value_range,x_y_value_range)

        outlier_point = (random_x_value,random_y_value,random_z_value)
        list_of_random_3D_points[point, :] = outlier_point

    return list_of_random_3D_points

def create_two_random_planes(total_number_points: int=1000, z_value: int=.001, x_y_value_range: int=25, group_value: int=50) -> np.array:

    # this function creates a random panel
    # you give it total amount of points, where you want the z value to be, 
    # and a different value for the range of x,y values 
    # this makes it so you get a plane as opposed to like a cube or sphere or something weird
    # Sorry this function is messy I was trying to go quick

    amount_of_points_in_one_cluster = int(np.ceil(total_number_points/2))
    list_of_random_3D_points = np.zeros((amount_of_points_in_one_cluster,3))
    list_of_random_3D_points2 = np.zeros((amount_of_points_in_one_cluster,3))


    for point in range(amount_of_points_in_one_cluster):
        random_x_value = np.random.uniform(group_value,group_value+x_y_value_range)
        random_y_value = np.random.uniform(group_value,group_value+x_y_value_range)
        random_z_value = np.random.uniform(-z_value,z_value)

        random_point = (random_x_value,random_y_value,random_z_value)
        list_of_random_3D_points[point, :] = random_point

    for point in range(amount_of_points_in_one_cluster):
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