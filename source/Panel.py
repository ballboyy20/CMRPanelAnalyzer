from typing import Union, Optional
import numpy as np

class Panel:
    def __init__(self, name: Optional[str] = None, 
                 normal_vector: Optional[Union[np.array, tuple]] = None,
                 plane_equation: Optional[Union[np.array, tuple]] = None,
                 centroid: Optional[Union[np.array, tuple]] = None) -> None:
        
        # Check if plane_equation is provided and has exactly 4 elements
        if plane_equation is not None and len(plane_equation) != 4:
            raise ValueError("Plane equation passed into panel instance must have exactly 4 values: (A, B, C, D)")
        
        # Check is centroid has 3 values 
        if centroid is not None and len(centroid) != 3:
            raise ValueError("Centroid passed into panel instance must have exactly 3 values")
        
        self.plane_equation = np.array(plane_equation) if plane_equation is not None else None
        self.panel_centroid = np.array(centroid) if centroid is not None else None
        self.panel_name = name

        # Set the normal vector if provided
        if normal_vector is not None:
            if len(normal_vector) != 3:
                raise ValueError("Normal vector must have exactly 3 values: (x, y, z)")
            self.normal_unit_vector = np.array(normal_vector)

        # If normal vector is not provided but plane equation is, extract the normal vector from plane equation
        elif plane_equation is not None:
            self.normal_unit_vector = np.array([plane_equation[0], plane_equation[1], plane_equation[2]])
        else:
            self.normal_unit_vector = None

    def get_data_as_dict(self) -> dict:
        return {
            'name': self.panel_name,
            'normal vector': self.normal_unit_vector.tolist() if self.normal_unit_vector is not None else None,
            'best fit plane': self.plane_equation.tolist() if self.plane_equation is not None else None,
            'centroid': self.panel_centroid.tolist() if self.panel_centroid is not None else None
        }
    
    def plane_equation_to_string(self) -> str:
        '''Create a string in the form of Ax + By + Cz + D = 0'''

        if self.plane_equation is None:
            return "Plane equation is not defined."

        A, B, C, D = self.plane_equation
        equation_str = f"{A}x + {B}y + {C}z + {D} = 0"
        return equation_str