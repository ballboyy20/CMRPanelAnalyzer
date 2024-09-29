from typing import Any, Tuple, Union
import numpy as np


class Panel:
    def __init__(self, vector: Union[np.array, Tuple[float, float, float]], 
                 centroid: Union[np.array,Tuple[float, float, float]], 
                 name: str) -> None:
        self.normal_unit_vector = np.array(vector)
        self.panel_centroid = np.array(centroid)
        self.panel_name = name

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __getattribute__(self, vector: np.array) -> Any:
        return super().__getattribute__(vector)
    
    def __getattribute__(self, centroid: np.array) -> Any:
        return super().__getattribute__(centroid)
    
    def get_data_as_dict(self) -> dict:
        return {
            'name': self.panel_name,
            'normal vector': self.normal_unit_vector,
            'centroid': self.panel_centroid
        }