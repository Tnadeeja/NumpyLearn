import numpy as np
arr1 = np.array([1,2,3,4,5,6])
print(arr1)
print(arr1[0])
print(arr1[-1])
print(arr1[1:3])
print(arr1[1:])
print(arr1[0::2])

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)
print(arr2[1,0])
print(arr2[1,0:2])
print(arr2[:,2])

arr3 = np.array([[[1,2,3],[5,6,7]],[[4,5,6],[4,6,9]], [[7,8,9],[1,7,6]]])
print(arr3)
print(arr3[2,0,1])
print(arr3[1,1,2])
