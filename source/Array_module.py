from .Panel_module import Panel
from typing import List, Tuple, Union
import os
from .Scan_module import Scan
from .utilities import *
import numpy as np 



class Array:
    def __init__(self, json_filename: str = None, json_location_directory: str = None,) -> None:
        self.list_of_panels: List[Panel] = [] # Initialize an empty list of type Panel
        
        # If a JSON filename is provided, load panels from the JSON file to this instance of Array
        if json_filename:
            self.json_to_panels(json_filename, json_location_directory)
    
    def add_panel(self, panel: Panel) -> None:
        self.list_of_panels.append(panel) # Add a Panel obeject to the list of Panels
    
    def add_panels_from_3DScan(self,scan_object: Scan) -> None: #TODO add error handling, make sure that the Scan passed in actually has data, also consider moving this to the constructor
        '''Takes 3D scan object and creates panels from its data'''

        for cluster_name, cluster_plane_equation in scan_object.get_clusters():
            
            temp_plane_equation = cluster_plane_equation
            temp_panel = Panel(name=cluster_name, plane_equation= temp_plane_equation)
            self.add_panel(temp_panel)

    def count_panels(self) -> int:
        return len(self.list_of_panels)

    def compare_two_panels(self, first_panel_to_be_compared: int, second_panel_to_be_compared: int) -> float:
        
        if first_panel_to_be_compared > len(self.list_of_panels) or second_panel_to_be_compared > len(self.list_of_panels):
            raise ValueError("You are trying to compare two panels that are not in the array. Try increasing your cluster amount")
        
        panel_one = self.list_of_panels[first_panel_to_be_compared]
        panel_two = self.list_of_panels[second_panel_to_be_compared]

        vector_one = panel_one.normal_vector
        vector_two = panel_two.normal_vector

        # Ensure both vectors are 1D arrays of length 3
        if vector_one.shape != (3,) or vector_two.shape != (3,):
            raise ValueError("Normal vectors must have 3 elements")
        


        angle_between_panels = get_angle_between_two_vectors(vector_one, vector_two)

        return angle_between_panels
    
    
    
    def panels_to_json(self, filename: str, json_save_directory: str = None ) -> None:

        #TODO make it so that the previous file is not over written...this isn't urgent

        # Create an empty list to hold the panel dictionaries
        panel_data_as_dicts = []

        # Iterates through the list of Panel obejct, creates a dict from each panel, appends that dict to the list of dicts
        for panel in self.list_of_panels:
            panel_data_as_dicts.append(panel.get_data_as_dict())

        #TODO this function is kinda ugly, see what could be moved to utils

        # If a directory is provided, join it with the filename, otherwise save in the package directory
        if json_save_directory:
            # Create the directory if it doesn't exist 
            os.makedirs(json_save_directory, exist_ok=True)
            file_path = os.path.join(json_save_directory, filename)
        else:
            # Writes the list of dictionaries to a JSON file in the local directory is a different directory is not given
            file_path = os.path.join(os.path.dirname(__file__), filename)

        write_list_dicts_to_json(panel_data_as_dicts, file_path)

    def json_to_panels(self, json_filename: str, json_location_directory: str = None) -> None:
        # If no directory is provided, default to the source directory of this script
        if json_location_directory is None:
            json_location_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script

        # Construct the full path to the JSON file
        full_path = os.path.join(json_location_directory, json_filename)

        # Read data from the JSON file
        data_from_json = get_dict_from_json(full_path)

        for panel_dict in data_from_json:
            # Extract the name, normal vector, and centroid from the JSON and create a new panel object with that data
            new_panel_from_json = Panel(panel_dict['name'], panel_dict['normal vector'], panel_dict['best fit plane'], panel_dict['centroid'])

            # Add the newly created panel to the list of panels attribute
            self.add_panel(new_panel_from_json)



