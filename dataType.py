import numpy as np
x = np.array([1.4,2.4,3.0,4])
print(x)
print(x.dtype)

y = np.array([1,2,3,4],dtype=int)
print(y)
print(y.dtype)

z = np.array(['amal', 'nimal', 'kasun'])
print(z)
print(z.dtype)

q = x.astype('i')
print(q)