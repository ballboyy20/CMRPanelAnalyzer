from source.Array import *
from source.utilities import create_random_panel

def test_creating_a_list_Panel():
    test_panel1 = create_random_panel()
    test_panel2 = create_random_panel()
    test_panel3 = create_random_panel()

    test_array = Array()

    test_array.add_panel(test_panel1)
    test_array.add_panel(test_panel2)
    test_array.add_panel(test_panel3)

    assert test_array.count_panels() == 3