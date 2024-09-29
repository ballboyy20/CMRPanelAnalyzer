from source.Panel import Panel
from typing import List
import os
import json
from source.utilities import * 


class Array:
    def __init__(self) -> None:
        self.list_of_panels: List[Panel] = [] # Initialize an empty list of type Panel
        
    
    def add_panel(self, panel: Panel) -> None:
        self.list_of_panels.append(panel) # Add a Panel instance to the list of Panels

    def count_panels(self) -> int:
        return len(self.list_of_panels)

    def compare_two_panels(self, first_panel_to_be_compared: int, second_panel_to_be_compared: int) -> float: # TODO make this do something with two panels
        
        panel_one = self.list_of_panels[first_panel_to_be_compared]
        panel_two = self.list_of_panels[second_panel_to_be_compared]

        vector_one = panel_one.get_normal_vector
        vector_two = panel_two.get_normal_vector

        angle_between_panels = get_angle_between_two_vectors(vector_one, vector_two)

        return angle_between_panels
    
    def panels_to_json(self, filename: str) -> None:

        # Check if the file already exists and append a suffix if needed
        base_filename, extension = os.path.splitext(filename)
        counter = 1
        new_filename = filename

        while os.path.exists(new_filename):
            new_filename = f"{base_filename}_{counter}{extension}"
            counter += 1
            
        # Create an empty list to hold the panel dictionaries
        panel_data_as_dicts = []

        # Iterate through the list of Panel objects
        for panel in self.list_of_panels:
            panel_data_as_dicts.append(panel.get_data_as_dict())

        # Write the list of dictionaries to a JSON file
        with open(filename, 'w') as json_file:
            json.dump(panel_data_as_dicts, json_file, indent=4)



