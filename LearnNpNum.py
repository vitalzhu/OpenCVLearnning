import numpy as np


a1 = np.array([1,2,3])
a2 = np.array([[1,2,3],[3,4,5]])

print(a1)
print(a2)

a = np.array([0,1,2,3,4,5,6,7,8,9])

print(len(a))
print(np.arange(0,len(a),1))
print(np.arange(len(a),0,-1))

print(a2.ndim)
print(a2.dtype)

arraySlice = a[:3]
print(arraySlice)

sliceIn = a[0:10:2]
print(sliceIn)

print('--------------------------')

A = np.random.rand(16).reshape((4,4))
print(A)


