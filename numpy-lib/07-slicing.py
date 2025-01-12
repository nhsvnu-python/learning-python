import numpy as np

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

print(x)
# slicing
z = x[1:4, 1:3]

print('After slicing, our array becomes:')
print(z)

# using advanced index for column
y = x[1:4, [1, 2]]

print('Slicing using advanced index for column:')
print(y)
