import numpy as np
a = np.zeros((10, 2)) # tạo ma trận don vi voi so dong la 10, so cot la 2
print(a)

b = a.T
print(b)

c = np.arange(6)
print(c)

print(c.reshape((3, 2)))

print(c.reshape((2, 3)))

print(c.reshape((2, -1)))  # -1 có nghĩa là kích thước còn lại tự suy diễn

print(c.reshape((6, -1)))

d = np.zeros((3, 3))
print(d)
#print(d.reshape((2, -1)))  # Không thành công vì 3 x 3 không chia hết cho 2

# Constructs 3D array
array = np.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n", array)
