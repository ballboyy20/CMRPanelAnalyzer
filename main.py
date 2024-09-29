from source.Panel import Panel
from source.Array import Array
from source.utilities import *

print("Hello world")
print("This is going to analyze some scans :) ")

test_array = Array()
panel1 = create_random_panel()
panel2 = create_random_panel()
panel3 = create_random_panel()

test_array.add_panel(panel1)
test_array.add_panel(panel3)
test_array.add_panel(panel2)

test_array.panels_to_json('WORKING')