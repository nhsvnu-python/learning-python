# create array
from numpy import array
# create array
l = [1.0, 2.0, 3.0]
a = array(l)
# display array
print(a)
# display array shape
print(a.shape)
# display array data type
print(a.dtype)

# create empty array: array with number random
from numpy import empty
b = empty([3,3])
print(b)

# create zero array
from numpy import zeros
c = zeros([3,5])
print(c)

# create one array
from numpy import ones
d = ones([5, 5])
print(d)

# ma trận đơn vị
from numpy import eye
e = eye(5, 4)
print(e)

# create two-dimensional array
# list of data
data = [[11, 22],
[33, 44],
[55, 66]]
# array of data
data = array(data)
print(data)
print(type(data))