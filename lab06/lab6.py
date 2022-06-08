import math as m
import numpy as np

def kowariancja(matrix):
    return np.dot(matrix.T,matrix)

def odwrotnosc(matrix):
    return np.linalg.inv(matrix)

def lewa_odw(matrix):
    kow = kowariancja(matrix)
    odw = odwrotnosc(kow)
    return np.dot(odw,matrix.T)
  
def regresja(matrix):
    matrix_x=np.array([[1,x[0]]for x in matrix])
    matrix_y=np.array([x[1]for x in matrix])
    lewa_odwr = lewa_odw(matrix_x)
    return np.dot(lewa_odwr,matrix_y) 

print(regresja(np.array([[1,2],[3,4],[3,2],[8,4]])))