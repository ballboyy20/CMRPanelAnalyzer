import numpy as np
import random
from source.Panel import Panel
import json

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
    normal_vector = (random.uniform(0.0, 10.0), 
                     random.uniform(0.0, 10.0), 
                     random.uniform(0.0, 10.0))
    
    # Generate random centroid with values between 0 and 10
    centroid = (random.uniform(0.0, 10.0), 
                random.uniform(0.0, 10.0), 
                random.uniform(0.0, 10.0))

    random_panel = Panel(normal_vector, centroid, panel_name)

    return random_panel

def write_list_dicts_to_json(list_of_dicts: dict, filename: str) -> None: #NOT TESTED
    
    with open(filename, 'w') as json_file:
                json.dump(list_of_dicts, json_file, indent=4)

def get_dict_from_json(json_filename: str) -> dict: #NOT TESTED
    
    with open(json_filename, 'r') as json_file:
        data_from_json = json.load(json_file)

    return data_from_json

# Trevor suggested that we make a conversion function that takes any 
# form of an array and converts it to numpy or something that we choose