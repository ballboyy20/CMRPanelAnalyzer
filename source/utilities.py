import numpy as np

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


# TODO: Implement this function
# This function is used by the 3DScan module various times, in various places, on both the point list as a whole and then on the individually grouped points, and this is is her as a util
def find_outliers(points: np.array, method: str | None = 'trev_iter') -> np.array:
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

# TODO: Implement this function
def remove_outliers_trev_iter(points: np.array) -> np.array:
    pass

# TODO: Implement this function
def remove_outliers_ransac(points: np.array) -> np.array:
    pass
    


# Trevor suggested that we make a conversion function that takes any 
# form of an array and converts it to numpy or something that we choose