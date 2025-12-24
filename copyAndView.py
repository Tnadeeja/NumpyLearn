import numpy as np

x = np.array([1,2,3,4,5,6])
y = x.copy()
#copy
x[0]=9

print("With copy")
print(x)
print(y)

#view
z = np.array([1,2,3,4,5,6])
q = z.view()

z[0]=9

print("With view")
print(z)
print(q)