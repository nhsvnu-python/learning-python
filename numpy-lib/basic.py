import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.itemsize)


b = np.array([2,3,4])
print(b)
print(b.dtype)

c = np.array([1.2, 3.5, 5.1])
print(c.dtype)
