import numpy as np
from scipy.spatial import distance
pointA=np.array([2, 4, 6])
pointB=np.array([5, 1, 9])

#minkowski distance with p=2
minkowski_dist_p3=distance.minkowski(pointA,pointB,p=2)
print("Minkowski distance between pointA and pointB:",minkowski_dist_p3)

#similarity(inverse of distance)
similarity_minkowski=1/(1+minkowski_dist_p3)
print("Similarity between pointA and pointB:",similarity_minkowski)

#minkowski distance with p=3
minkowski_dist_p3=distance.minkowski(pointA,pointB,p=1)
print("Minkowski distance between pointA and pointB with p=1:",minkowski_dist_p3)

#similarity(inverse of distance)
similarity_minkowski=1/(1+minkowski_dist_p3)
print("Similarity between pointA and pointB with p=1:",similarity_minkowski)
