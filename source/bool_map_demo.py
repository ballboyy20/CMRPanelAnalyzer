import numpy as np

random_array = np.random.rand(1000, 3)
#print(random_array)

bool_map = np.full(random_array.shape[0], False)

bool_map[[0, 1, 2, 998, 999]] = True

print(random_array[bool_map][:, [0, 2]])

