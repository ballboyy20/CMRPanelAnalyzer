from source.Panel import Panel
from typing import List
import os
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




    def json_to_panels(self,json_filename: str) -> None:

        data_from_json = get_dict_from_json(json_filename)

        for panel_dict in data_from_json:
            # Extract the name, normal vector, and centroid from the json and create a new panel object with that data
            new_panel_from_json = Panel(panel_dict['name'],panel_dict['normal vector'],panel_dict['centroid'])

            # Add the newly created panel to the list of panels attribute
            self.add_panel(new_panel_from_json)



