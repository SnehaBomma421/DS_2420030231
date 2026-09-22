import numpy as np
from scipy.spatial import distance
pointA=np.array([2, 4, 6])
pointB=np.array([5, 1, 9])
#euclidien distance
euclidean_distance=distance.euclidean(pointA,pointB)
print("Euclidean distance between pointA and pointB:",euclidean_distance)   
#similarity(inverse of distance)
similarity_euclidean=1/(1+euclidean_distance)
print("Similarity between pointA and pointB:",similarity_euclidean)
