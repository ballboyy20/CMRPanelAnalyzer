from source.utilities import *

vector_three = (5.5, -6.5, 2.0)
vector_four = (-0.25, 0.64, 0.78)
result = get_angle_between_two_vectors(vector_three, vector_four)
print(result)


def test_get_angle_between_two_vectors_1():
    vector_one = (0.0, 0.0, 1.0)
    vector_two = (1.0, 0.0, 0.0)
    result = get_angle_between_two_vectors(vector_one, vector_two)
    assert result == 90.0  

def test_get_angle_between_two_vectors_2():
    vector_three = (5.5, -6.5, 2.0)
    vector_four = (-0.25, 0.64, 0.78)
    result = get_angle_between_two_vectors(vector_three, vector_four)
    assert round(result, 6) == 115.926256  # Rounded comparison for floating-point accuracy

def test_get_magnitude_of_vector_1():
    vector = (5.5, -6.5, 2.0)
    
    result = get_magnitude_of_vector(vector)
    assert round(result,5) == 8.74643