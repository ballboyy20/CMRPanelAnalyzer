import numpy as np
from source.Panel import Panel
from skspatial.objects import Plane
from scipy.spatial import ConvexHull
import pyransac3d
import json
import os

from sklearn.cluster import KMeans
import skspatial.objects as skobj
import skspatial.transformation as sktrf

def get_angle_between_two_vectors(vector_one, vector_two) -> float:
	"""This function will find the angle between two vectors. It has some error checking as well. """
	dot_product = np.dot(vector_two, vector_one)
	
	magnitude_one = get_magnitude_of_vector(vector_one)
	magnitude_two = get_magnitude_of_vector(vector_two)

	if magnitude_one == 0.0 or magnitude_two == 0.0:
		raise ValueError("One or both of the vectors have zero magnitude :( ")
	
	value = dot_product/(magnitude_one * magnitude_two)

	print(f"ANGLE BETWEEN TWO VECTORS INFO: Dot product: {dot_product}, Magnitude product: {magnitude_one * magnitude_two}, Value: {value}")
	value = np.clip(value, -1.0, 1.0)
	angle_in_radians = np.arccos(value)

	angle_in_degrees = np.rad2deg(angle_in_radians)

	return angle_in_degrees

def get_magnitude_of_vector(vector: tuple) -> float:
	magnitude = np.sqrt(np.square(vector[0]) + np.square(vector[1]) + np.square(vector[2]))
	return magnitude

def calc_centroid_from_points(point_array: np.array) -> np.array: #TODO test the crap out of this function
	 #This library will find the smallest polygon that encompasses
	 # the 3d points and find the centroids based on that
	 # we may consider flattening the data before finding the centroid...
	 # but it may not matter.
	hull = ConvexHull(point_array)
	
	hull_vertices = point_array[hull.vertices]
	
	centroid = np.mean(hull_vertices, axis=0)
	 
	return centroid

def calc_normal_vector_and_bestfit_plane(point_array: np.array) -> np.array: #TODO test this function more
	 
	plane_of_best_fit = Plane.best_fit(point_array)
	normal_vector = plane_of_best_fit.normal
	
	return normal_vector, plane_of_best_fit

def write_list_dicts_to_json(list_of_dicts: dict, filename: str) -> None: #NOT TESTED WITH PY TEST
	
	with open(filename, 'w') as json_file:
				json.dump(list_of_dicts, json_file, indent=4)

def get_dict_from_json(json_filename: str, directory: str = None) -> dict: #NOT TESTED WITH PY TEST
	
	# If a directory is provided, join it with the filename to create the full path
	if directory:
		file_path = os.path.join(directory, json_filename)
	else:
		# Default to the current working directory if no directory is provided
		file_path = json_filename

	# Open and load the JSON file from the constructed file path
	with open(file_path, 'r') as json_file:
		data_from_json = json.load(json_file)

	return data_from_json

def remove_outliers_ransac(points: np.array) -> np.array:

	# Initialize RANSAC for plane fitting
	plane_ransac = pyransac3d.Plane()

	# Fit a plane to the data points
	equation_for_plane, inliers = plane_ransac.fit(points, thresh=.01, maxIteration=1000)

	# Get the outliers
	outliers = np.setdiff1d(np.arange(points.shape[0]), inliers)
	boolean_mask = np.zeros(points.shape[0],dtype=bool)
	boolean_mask[inliers] = True
	boolean_mask[outliers] = False

	return boolean_mask

def identify_clusters_Kmeans(data: np.array, amount_clusters: int, return_centroids: bool = False) -> np.array: # TODO test this function
	
	kmeans = KMeans(n_clusters=amount_clusters)
	
	# Perform clustering
	cluster_mask = kmeans.fit_predict(data)
	
	# Conditionally return centroids
	if return_centroids:
		centroids = kmeans.cluster_centers_
		return cluster_mask, centroids
	else:
		return cluster_mask


# # TODO: implement original clustering algorithm in 3d space (without projection)
# def kmeans_clusters(point_array: np.array) -> tuple(np.array, np.array, np.array):
#       pass

def get_clusters(point_cloud, best_fit_plane, n_clusters, cluster_similarity=2.5, km_iter_lim=20, center_type='spatial', verbose=True):
	# """
	# Observing a set of points, project them into their own plane of best fit, then use
	# k-means to identify the point groups selected by the user during preprocessing.
	# Verify that all clusters are similarly sized (to a tolerance), then return them.
	
	# :param point_cloud: skspatial.objects.Points object or a NumPy array where a list of vertices is provided
	# :param best_fit_plane: skspatial.objects.Plane object, for this point cloud
	# :param n_clusters: Integer value for the number of groups to search for, passed along to k-means
	# :param cluster_similarity: Float value, if the ratio of the largest group to the smallest one is greater than this, k-means will be reinitialized
	# :param km_iter_lim: After this many iterations, raise a TimeoutError, since satisfactory clusters couldn't be formed
	# :param center_type: 'spatial' to calculate cluster centers as the middle points of the extremes
	# 	in each dimension, 'centroid' to use the centroids produced by the k-means algorithm itself
	# :param verbose: If True, give real time data as clusters are formed
	# :return: labels, centroids, trans_proj_cloud: For all points, labels about which cluster the point would
	# 	be grouped into. Central positions for each cluster. The 2D transformed coordinates that were used.
	# """
	# # Randomly produce x and y vectors that form an orthonormal basis with the normal of the plane of best fit
	# b1, b2 = generate_orthonormal_basis(best_fit_plane)
	# # Transform the points into a coordinate system with the previously generated unit vectors (and the
	# # plane of best fit's normal vector) as bases and the plane of best fit's point as the origin. Discard
	# # the z coordinates (out of the plane), effectively projecting the points onto a 2D plane.
	# trans_proj_cloud = sktrf.transform_coordinates(point_cloud, best_fit_plane.point, (b1, b2, best_fit_plane.normal))[:, 0:2]
	

	# if not isinstance(n_clusters, int):
	# 	raise UserWarning("k-means requires an integer for the number of clusters, but you provided ", n_clusters)
	# iteration = 1
	# # Keep reinitializing k-means until clusters are formed that are close enough in size
	# while True:
	# 	if iteration > km_iter_lim:
	# 		raise TimeoutError(f"With {iteration} iterations, surpassed the limit set for k-means. Try adjusting"
	# 						   f"cluster_similarity to expand or shrink the expected similarity in size between"
	# 						   f"clusters, or increasing the allowed number of iterations with km_iter_lim")
	# 	# Initializing
	# 	km_model = KMeans(n_clusters=n_clusters)
	# 	# Fitting the model to our 2D transformed point cloud and grouping it. Makes a 1D array,
	# 	# where each element is an integer, representing the assigned cluster
	# 	# of the point at the corresponding row of the point cloud passed to the model.
	# 	labels = km_model.fit_predict(trans_proj_cloud)
	# 	# Make a k * n shaped array, where n is the number of dimensions of our coordinates,
	# 	# and k is the number of clusters, where each column (n) contains the maximal distance
	# 	# in that dimension for all points of a given cluster (by row, k)
	# 	ranges = np.array([np.ptp(trans_proj_cloud[labels == label], axis=0) for label in np.unique(labels)])
	# 	# Make two n shaped array, respectively containing the smallest and largest cluster sizes in each dimension
	# 	min_ranges = np.min(ranges, axis=0)
	# 	max_ranges = np.max(ranges, axis=0)
	# 	if verbose:
	# 		print("Smallest cluster size (x, y): ", min_ranges)
	# 		print("Largest cluster size (x, y): ", max_ranges)
	# 	# For all dimensions (columns), if the maximum range is less than 120% of the minimum range, the model must have made
	# 	# even groups that catch all panels. When this is done, simply exit the loop and use the latest assigned group values.
	# 	if np.all(max_ranges <= min_ranges * cluster_similarity):
	# 		if verbose:
	# 			print(f"After {iteration} iterations, found clusters such that the largest group's size is within {100*cluster_similarity}% of the that of the smallest group.")
	# 		break
	# 	else:
	# 		if verbose:
	# 			print("There exists a dissimilarity in size greater than the limit of ", 100*cluster_similarity, "%")
	# 			print("Re-initializing k-means to try again...")
	# 		iteration += 1
	# # When we've found a satisfactory grouping, get central values for each group.
	# centroids_list = []
	# for label_i in np.unique(labels):
	# 	cluster_map = (labels == label_i)
	# 	cluster_points = trans_proj_cloud[cluster_map, :]
	# 	# Find the minimums and maximums in each dimension
	# 	min_corner = np.min(cluster_points, axis=0)
	# 	max_corner = np.max(cluster_points, axis=0)
	# 	# The middle point between the minimums and maximums will be our spatial center for this label
	# 	spatial_center = np.mean((min_corner, max_corner), axis=0)
	# 	centroids_list.append(spatial_center)
	# centroids = np.array(centroids_list)

	# # The k-means model does produce centroids, but their ordering is unknown (but likely the same
	# # order as the labels counting up). It also likely leans towards higher densities of points
	# # (which I'm now realizing is mostly irrelevant, since in-plane translation of the selected
	# # points relative to the real, physical panel is assumed to be imprecise already)
	# #centroids = km_model.cluster_centers_

	# return labels, centroids, trans_proj_cloud
	 pass

# This is used by k-means to help create projections
def generate_orthonormal_basis(plane, seed=None):
	# """
	# Following function was generated by ChatGPT then simplified to use skspatial objects and methods. It's
	# basic purpose is to generate two random vectors that are orthogonal with the normal of our plane.

	# :param plane: An skspatial.objects.Plane object
	# :param seed: An integer value to get repeatable results
	# :return: basis_vector_1, basis_vector_2: Two vectors that are orthogonal with the normal of the input plane
	# """
	# if seed is not None:
	# 	np.random.seed(seed)
	# # Normalize the normal to our plane (make it a vector with a magnitude of one, a unit vector)
	# plane_norm = plane.normal.unit()

	# # Generate a completely random vector in 3d
	# random_vector = np.random.randn(3)
	# # Make sure the random vector is not parallel to the normal vector of our plane
	# # (which is basically impossible as a random float, but we like being thorough)
	# while np.allclose(np.dot(random_vector, plane_norm), 0):
	# 	random_vector = np.random.randn(3)
	
	# # Project the random vector onto the plane to make it orthogonal
	# # to the normal vector, then normalize it to a unit vector
	# basis_vector_1 = plane.project_vector(skobj.Vector(random_vector)).unit()
	
	# # Create the second basis vector by taking the cross product of the normal and the first basis
	# basis_vector_2 = skobj.Vector(np.cross(plane_norm, basis_vector_1)).unit()
	
	# return basis_vector_1, basis_vector_2
	pass




# Trevor suggested that we make a conversion function that takes any 
# form of an array and converts it to numpy or something that we choose