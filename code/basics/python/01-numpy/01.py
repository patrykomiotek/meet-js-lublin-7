import numpy as np

a = np.array([6, 7, 8])
b = np.array([1, 2, 3])
c = np.array([[2], [4], [6]])

d = np.array([
    [1, 2, 3], [4, 5, 6]
])
print(d)

print(a + b)
print(b / 2)

np.array([1, 2, 3.0])
#array([ 1.,  2.,  3.])

# np.array([[1, 2], [3, 4]])
# array([[1, 2],
#        [3, 4]])

# Minimum dimensions 2:
np.array([1, 2, 3], ndmin=2)
# array([[1, 2, 3]])

# Type provided
np.array([1, 2, 3], dtype=complex)
# array([ 1.+0.j,  2.+0.j,  3.+0.j])
