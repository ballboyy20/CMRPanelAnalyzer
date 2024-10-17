from typing import Any, Tuple, Union
import numpy as np


class Panel:
    def __init__(self, name: str, vector: Union[np.array, Tuple[float, float, float]], 
                 best_fit_plane: Union[np.array, Tuple[float, float, float]],
                 centroid: Union[np.array,Tuple[float, float, float]]) -> None:
        self.normal_unit_vector = np.array(vector)
        self.panel_centroid = np.array(centroid)
        self.best_fit_plane = np.array(best_fit_plane)
        self.panel_name = name

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __getattribute__(self, vector: np.array) -> Any:
        return super().__getattribute__(vector)
    
    def __getattribute__(self, centroid: np.array) -> Any:
        return super().__getattribute__(centroid)
    
    def __getattribute__(self, best_fit_plane: np.array) -> Any:
        return super().__getattribute__(best_fit_plane)
    
    def get_data_as_dict(self) -> dict: #FIXME this function is breaking the write_list_dicts_to_json function in utilities
        return {
            'name': self.panel_name,
            'normal vector': self.normal_unit_vector.tolist(),  # Convert numpy array to list so that json likes it
            'best fit plane': self.best_fit_plane.tolist(),
            'centroid': self.panel_centroid.tolist()
        }