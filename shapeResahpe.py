import numpy as np
print("ABOUT SHAPE")
x = np.array([1, 2, 3, 4, 5])
print(x)
print(x.shape)

y = np.array([[1,2],[3,4],[5,6],[7,8]])
print(y)
print(y.shape)

z = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(z)
print(z.shape)

q = np.array([1,2,3,4,5], ndmin=5)
print(q)
print(q.shape)

print("ABOUT RESHAPE")
t = np.array([1,2,3,4,5,6,7,8,9])
print(t)

g = t.reshape(3,3)
f = t.reshape(9,1)

print(g)
print(f)

a = np.array([1,2,3,4,5,6,7,8])
b = a.reshape(2,2,2)
print(a)
print(b)

k = np.array([[1,2],[3,4],[5,6],[7,8]])
print(k)
print(k.reshape(-1))