import numpy as np
print(np.__version__)

#1D
x = np.array([1,2,3,4])
print("1D array: ", x)
print(x.ndim)

#2D
y = np.array([[1,2,3,4], [5,6,7,8]])
print("2D array: ", y)
print(y.ndim)

#3D
z = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print("3D array: ", z)
print(z.ndim)

#4D
q = np.array([[[[1,2], [3,4], [5,6], [7,8]]]])
print("4D array: ", q)
print(q.ndim)

a = np.array([1,2,3,4], ndmin=4)
print("4D array: ", a)
print(a.ndim)

