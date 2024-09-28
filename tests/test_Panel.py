from source.Panel import *

def test_intialize_a_panel1():
    panel_name = "Test Panel 1"
    test_normal_vector = (5.5, -6.5, 2.0) # Initialize as tuple
    test_centroid = (0.0, 0.0, 0.0)       # Initialize as tuple

    test_panel = Panel(test_normal_vector, test_centroid, panel_name)

    assert test_panel.panel_name == panel_name # assert will only pass if the function returns true
    assert np.array_equal(test_panel.normal_unit_vector, test_normal_vector) # assert will only pass if the function returns true
    assert np.array_equal(test_panel.panel_centroid, test_centroid) # assert will only pass if the function returns true

def test_initialize_a_panel2():
    panel_name = "Test Panel 2"
    test_normal_vector = np.array([5.5, -6.5, 2.0])  # Initialize as np.array
    test_centroid = np.array([0.0, 0.0, 0.0])        # Initialize as np.array

    test_panel = Panel(test_normal_vector, test_centroid, panel_name)

    assert test_panel.panel_name == panel_name  # Assert will only pass if the function returns true
    assert np.array_equal(test_panel.normal_unit_vector, test_normal_vector)  # Assert will only pass if the function returns true
    assert np.array_equal(test_panel.panel_centroid, test_centroid)  # Assert will only pass if the function returns true