from source.Panel_module import *

def test_intialize_a_panel1():
    
    panel_name = "Test Panel 1"
    test_normal_vector = (5.5, -6.5, 2.0) # Initialize as tuple
    test_centroid = (0.0, 0.0, 0.0)       # Initialize as tuple
    expected_best_fit_plane = (4.0, 5.0, 6.0)
    test_panel = Panel(panel_name, test_normal_vector,expected_best_fit_plane, test_centroid)

    assert test_panel.panel_name == panel_name
    assert np.array_equal(test_panel.normal_unit_vector, test_normal_vector) 
    assert np.array_equal(test_panel.panel_centroid, test_centroid) 

def test_initialize_a_panel2():

    panel_name = "Test Panel 2"
    test_normal_vector = np.array([5.5, -6.5, 2.0])
    test_centroid = np.array([0.0, 0.0, 0.0])
    expected_best_fit_plane = (4.0, 5.0, 6.0)

    test_panel = Panel(panel_name, test_normal_vector, expected_best_fit_plane, test_centroid)

    assert test_panel.panel_name == panel_name, "Panel name does not match"
    assert np.array_equal(test_panel.normal_unit_vector, test_normal_vector), "Normal vector does not match"
    assert np.array_equal(test_panel.panel_centroid, test_centroid), "Centroid does not match"

def test_initialize_a_panel3():

    panel_name = "Test Panel 3"
    test_normal_vector = np.array([5.5, -6.5, 2.0])
    test_centroid = np.array([0.0, 0.0, 0.0])
    expected_plane_equation = np.array([4.0, 5.0, 6.0, 600])

    test_panel = Panel(panel_name, test_normal_vector, expected_plane_equation, test_centroid)

    assert test_panel.panel_name == panel_name, "Panel name does not match"
    assert np.array_equal(test_panel.normal_unit_vector, test_normal_vector), "Normal vector does not match"
    assert np.array_equal(test_panel.panel_centroid, test_centroid), "Centroid does not match"
    assert np.array_equal(test_panel.plane_equation,expected_plane_equation), "Plane Equation does not match"

def test_initialize_a_panel4():

    panel_name = "Test Panel 4"
    expected_plane_equation = np.array([4.0, 5.0, 6.0, 600])
    expected_normal_vector = np.array([expected_plane_equation[0],expected_plane_equation[1],expected_plane_equation[2]])

    test_panel = Panel(panel_name, plane_equation=expected_plane_equation)

    assert test_panel.panel_name == panel_name, "Panel name does not match"
    assert np.array_equal(test_panel.normal_unit_vector, expected_normal_vector), "Normal vector does not match"
    assert np.array_equal(test_panel.plane_equation,expected_plane_equation), "Plane Equation does not match"

def test_get_data_as_dict():

    expected_vector = (1.0, 2.0, 3.0)
    expected_best_fit_plane = (4.0, 5.0, 6.0)
    expected_centroid = (7.0, 9.0, 9.0)
    expected_name = "Test Panel 3"

    test_panel = Panel(name=expected_name,vector=expected_vector, best_fit_plane=expected_best_fit_plane,centroid=expected_centroid)

    panel_data = test_panel.get_data_as_dict()

    assert panel_data['name'] == expected_name, "Panel name does not match"
    assert np.array_equal(panel_data['normal vector'], test_panel.normal_unit_vector), "Normal vector does not match"
    assert np.array_equal(panel_data['best fit plane'],test_panel.best_fit_plane), "Best fit plane didn't work"
    assert np.array_equal(panel_data['centroid'], test_panel.panel_centroid), "Centroid does not match"