import numpy as np
from numpy.ma.extras import ndenumerate

arr1 = np.array([1,2,3,4,5,6,7])
for i in arr1:
    print(i)

print("-----------")

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in arr2:
    for j in i:
        print(j)

print("OR")
for i in np.nditer(arr2):
    print(i)

for i, j in ndenumerate(arr2):
    print(i,j)