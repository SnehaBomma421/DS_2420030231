import numpy as np
p=np.array([1,2,3,4])
print(p[0])
print(p[3])
q=np.array([[1,2,3,4],[5,6,7,8]])
print(q[0,1])
s=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(s[0,1,2])
#negative indexing
print(p[-1])
print(q[0,-1])
#array slicing
print(p[1:3])
print(p[:3])
print(p[2:])   