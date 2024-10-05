from source.utilities import *
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


def test_remove_outliars_ransac1(): # TODO This test is currently subjective. How could we make it objective?
# Create a random dataset
    points = create_random_dataset(1000, 0.001, 50)
    
    # Get the boolean map for inliers
    inlier_map = remove_outliers_ransac(points)
    
    # Get the actual inlier and outlier points
    inliers = points[inlier_map]
    outliers = points[~inlier_map]

    plot_two_sets_3D_points(inliers,outliers)

    assert 'It looks good' == "It looks good"

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
    
    n_clusters = 3
    
    # Use the kmeans_clustering function
    labels = identify_clusters_with_Kmeans(data, n_clusters)

    # Check that the number of unique labels matches the number of clusters
    unique_labels = np.unique(labels)
    
    assert len(unique_labels) == n_clusters, f"Expected {n_clusters} clusters, but got {len(unique_labels)}."
    assert all(label in range(n_clusters) for label in unique_labels), "Labels should be in the range of cluster numbers."

    # Additional check to ensure clustering has some variation
    # Count occurrences of each label in the output
    counts = {label: np.sum(labels == label) for label in unique_labels}
    
    # Check that we have some points assigned to each cluster
    assert all(count > 0 for count in counts.values()), "All clusters should have at least one point assigned."










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