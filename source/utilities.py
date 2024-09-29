import numpy as np
import random
from source.Panel import Panel
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
    normal_vector = (random.uniform(0.0, 10.0), 
                     random.uniform(0.0, 10.0), 
                     random.uniform(0.0, 10.0))
    
    # Generate random centroid with values between 0 and 10
    centroid = (random.uniform(0.0, 10.0), 
                random.uniform(0.0, 10.0), 
                random.uniform(0.0, 10.0))

    random_panel = Panel(panel_name,normal_vector, centroid)

    return random_panel

def write_list_dicts_to_json(list_of_dicts: dict, filename: str) -> None: #NOT TESTED
    
    with open(filename, 'w') as json_file:
                json.dump(list_of_dicts, json_file, indent=4)

def get_dict_from_json(json_filename: str, directory: str = None) -> dict:
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

# Trevor suggested that we make a conversion function that takes any 
# form of an array and converts it to numpy or something that we choose