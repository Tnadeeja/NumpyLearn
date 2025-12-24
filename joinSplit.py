import numpy as np
print("JOIN")
arr1 = np.array([1,2,5])
arr2 = np.array([3,4,9])

new = np.concatenate((arr1,arr2))
print(new)

arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[4,5,6],[7,8,9]])

new2 = np.concatenate((arr3,arr4), axis=1)
print(new2)

print("SPLIT")
arr5 = np.array([1,2,3,4,5,6,7,8,9])
new3 = np.array_split(arr5, 3)
print(new3)