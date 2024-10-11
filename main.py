from source.Panel import Panel
from source.Array import Array
from tests.test_utilities import *
from source.Visualizer import *
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print('hello world')

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Generate random 3D points
points = create_random_dataset()

# Compute the convex hull
hull = ConvexHull(points)

# Extract the vertices of the convex hull
hull_vertices = points[hull.vertices]

# Calculate the centroid of the convex hull vertices
centroid = np.mean(hull_vertices, axis=0)

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='blue', label='Points')

# Plot the convex hull
for simplex in hull.simplices:
    ax.plot3D(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'k-')

# Plot the centroid
ax.scatter(centroid[0], centroid[1], centroid[2], color='red', s=100, label='Centroid', marker='o')

# Set the same scale for all axes
max_range = np.array([points[:, 0].max() - points[:, 0].min(),
                      points[:, 1].max() - points[:, 1].min(),
                      points[:, 2].max() - points[:, 2].min()]).max() / 2.0

mid_x = (points[:, 0].max() + points[:, 0].min()) * 0.5
mid_y = (points[:, 1].max() + points[:, 1].min()) * 0.5
mid_z = (points[:, 2].max() + points[:, 2].min()) * 0.5

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Customize the plot
ax.set_title('Convex Hull and Centroid')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

plt.show()