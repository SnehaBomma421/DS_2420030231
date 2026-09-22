import numpy as np
from scipy.spatial import distance
pointA=np.array([2, 4, 6])
pointB=np.array([5, 1, 9])
manhattan_distance=distance.cityblock(pointA,pointB)
print("Manhattan distance between pointA and pointB:",manhattan_distance)   
#similarity(inverse of distance)
similarity_manhattan=1/(1+manhattan_distance)
print("Similarity between pointA and pointB:",similarity_manhattan)