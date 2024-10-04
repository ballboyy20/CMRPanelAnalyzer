from source.Panel import Panel
from source.Array import Array
from source.utilities import *
import numpy as np
import numpy as np

print('hello world')


    
points = create_random_dataset(10000,.001,50)
inliers_indices, outliers_indices, best_eq = remove_outliers_ransac(points)
plot_3d_points(points)

# Get the actual inlier and outlier points
inliers = points[inliers_indices]
outliers = points[outliers_indices]

# Display the plane equation and inliers
print("Best plane equation (Ax + By + Cz + D = 0):", best_eq)
print("Inliers:", inliers)
print("Outliers:", outliers)

plot_two_sets_3D_points(inliers,outliers)