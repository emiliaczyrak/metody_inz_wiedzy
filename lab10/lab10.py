import numpy as np
import math as m

#ortogonalna
a = np.array([[1.,1.,1.,1.,1.,1.,1.,1.],
              [1.,1.,1.,1.,-1.,-1.,-1.,-1],
              [1.,1.,-1.,-1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,1.,1.,-1.,-1.],
              [1.,-1.,0.,0.,0.,0.,0.,0.],
              [0.,0.,1.,-1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,1.,-1.,0.,0.],
              [0.,0.,0.,0.,0.,0.,1.,-1.]])

b = np.dot(a,a.T)
c = []
temp = 0
for row in a:
    c.append(np.dot(np.array(row),np.array(row).T))
print(b)
print(all(c==np.diag(b)))

d = []
for i in range(len(a[0])):
    d.append(a[i]*(1/m.sqrt(c[i])))
d = np.array(d)
print(d.T) 
print(np.linalg.inv(d)) 
print(np.dot(d,np.linalg.inv(d)))
print(np.diag([1.,1.,1.,1.,1.,1.,1.,1.]).all()==np.dot(d,np.linalg.inv(d)).all())

ones = np.diag([1.,1.,1.,1.,1.,1.,1.,1.])
va=np.array([8.,6.,2.,3.,4.,6.,6.,5.])
vb=np.dot(d,va)
print(vb)