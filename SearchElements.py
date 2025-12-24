import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

x = np.where(arr==3)
print(x)

y = np.where(arr%2==0)
print(y)

arr2 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr2)
t = np.where(arr2==3)
print(t)

print("SearchSorted")

arr3 = np.array([1,2,5,7,8,9])
print(np.searchsorted(arr3,3))
print(np.searchsorted(arr3,3, side='right'))
print(np.searchsorted(arr3,[3,4,10]))