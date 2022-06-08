from numpy import array
from scipy.linalg import svd
A = array([[1, 2], [2, 0], [3, 1]])
print(A)

U, s, VT = svd(A)
print(U)
print(s)
print(VT)