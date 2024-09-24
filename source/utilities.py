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


# Trevor suggested that we make a conversion function that takes any 
# form of an array and converts it to numpy or something that we choose