from source.Panel import *

def test_intialize_a_panel1():
    panel_name = "Test Panel 1"
    test_normal_vector = (5.5, -6.5, 2.0) # Initialize as tuple
    test_centroid = (0.0, 0.0, 0.0)       # Initialize as tuple

    test_panel = Panel(panel_name, test_normal_vector, test_centroid)

    assert test_panel.panel_name == panel_name # assert will only pass if the function returns true
    assert np.array_equal(test_panel.normal_unit_vector, test_normal_vector) # assert will only pass if the function returns true
    assert np.array_equal(test_panel.panel_centroid, test_centroid) # assert will only pass if the function returns true

def test_initialize_a_panel2():
    panel_name = "Test Panel 2"
    test_normal_vector = np.array([5.5, -6.5, 2.0])  # Initialize as np.array
    test_centroid = np.array([0.0, 0.0, 0.0])        # Initialize as np.array

    test_panel = Panel(panel_name, test_normal_vector, test_centroid)

    assert test_panel.panel_name == panel_name, "Panel name does not match"
    assert np.array_equal(test_panel.normal_unit_vector, test_normal_vector), "Normal vector does not match"
    assert np.array_equal(test_panel.panel_centroid, test_centroid), "Centroid does not match"

def test_get_data_as_dict():
    # Known values for the test
    expected_vector = (1.0, 2.0, 3.0)
    expected_centroid = (4.0, 5.0, 6.0)
    expected_name = "Test Panel 3"

    # Create an instance of the Panel class
    test_panel = Panel(name=expected_name,vector=expected_vector, centroid=expected_centroid)

    # Get the data as a dictionary
    panel_data = test_panel.get_data_as_dict()

    # Assertions to check if the returned dictionary matches expected values
    assert panel_data['name'] == expected_name, "Panel name does not match"
    assert np.array_equal(panel_data['normal vector'], test_panel.normal_unit_vector), "Normal vector does not match"
    assert np.array_equal(panel_data['centroid'], test_panel.panel_centroid), "Centroid does not match"