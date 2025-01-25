from source.Array_module import *
from source.Panel_module import Panel
from test_utilities import create_random_panel
import random

def test_creating_a_list_Panel():
	test_panel1 = create_random_panel()
	test_panel2 = create_random_panel()
	test_panel3 = create_random_panel()

	test_array = Array()

	test_array.add_panel(test_panel1)
	test_array.add_panel(test_panel2)
	test_array.add_panel(test_panel3)

	assert test_array.count_panels() == 3
	
def test_add_raw_panel():
	name = 'raw panel'
	normal_vector = (random.uniform(0.0, 10.0), 
					 random.uniform(0.0, 10.0), 
					 random.uniform(0.0, 10.0))
	
	centroid = (random.uniform(0.0, 10.0), 
				random.uniform(0.0, 10.0), 
				random.uniform(0.0, 10.0))
	test_array = Array()
	test_array.add_raw_panel(name,normal_vector,centroid)
	amount_of_panels = test_array.count_panels()

	assert amount_of_panels == 1

def test_compare_two_panels():
	plane_equation_one = [1,1,0,0]
	plane_equation_two = [0,0,1,7]

	test_panel_one = Panel(name=0,plane_equation=plane_equation_one)
	test_panel_two = Panel(name=1,plane_equation=plane_equation_two)

	test_array = Array()
	test_array.add_panel(test_panel_one)
	test_array.add_panel(test_panel_two)

	test_array.compare_two_panels(0,1)
	


# def test_panels_to_json_and_read():
#     # Setup
#     test_array = Array()
#     panel1 = create_random_panel()
#     panel2 = create_random_panel()
#     panel3 = create_random_panel()

#     test_array.add_panel(panel1)
#     test_array.add_panel(panel2)
#     test_array.add_panel(panel3)

#     # Save panels to JSON
#     test_json_filename = 'test_panels.json'
#     test_array.panels_to_json(test_json_filename)

#     # Create a new Array instance to read from JSON
#     new_array = Array()
#     new_array.json_to_panels(test_json_filename, test_json_filename)

#     # Verify that the number of panels matches
#     assert new_array.count_panels() == test_array.count_panels(), "Panel count does not match after reading from JSON."

#     # Verify that each panel's data matches
#     for original_panel, read_panel in zip(test_array.list_of_panels, new_array.list_of_panels):
#         assert original_panel.panel_name == read_panel.panel_name, "Panel names do not match."
#         assert np.array_equal(original_panel.normal_unit_vector, read_panel.normal_unit_vector), "Normal vectors do not match."
#         assert np.array_equal(original_panel.panel_centroid, read_panel.panel_centroid), "Centroids do not match."

#     # Clean up: remove the test JSON file after the test
#     os.remove(test_json_filename)