import math as m
import numpy as np

def projekcja(u,v):
    u_v = np.dot(u.T,v)
    u_u = np.dot(u.T,u)
    if u_u==0:
        return u
    return (u_v/u_u)*u


def matrix_dl(u):
    return m.sqrt(np.dot(u.T,u))

def q_dekompozycja(a):
    v_list=[ [ x[i] for x in a ] for i in range(len(a[1])) ]
    u_list = []
    q = []
    
    for v in v_list:
        v = np.array(v)
        sum_proj = 0
        for u_x in u_list:
            u_x = np.array(u_x)
            sum_proj+=projekcja(u_x, v)
        u = v - sum_proj
        u_list.append(u)
        if matrix_dl(u)==0:
            e=u
        else:
            e = (1/matrix_dl(u))*u
        q.append(e)
        
    return np.array(q).T

def matrix_plus_1(a):
    q = q_dekompozycja(a)
    a2 = np.dot(q.T,a)
    a2 = np.dot(a2,q)
    return a2

def matrix_wlasne(a):
    a2 = a
    i=0
    while (np.diag(a2)-np.dot(a2,np.ones((5,1))).T).all()>0.001 :
        a2 = matrix_plus_1(a2)
        i=i+1
    return np.diag(a2)
      
a=np.array([[1.,2.,3.,4.,5.],[2.,2.,3.,4.,5.],[3.,3.,3.,4.,5.],[4.,4.,4.,4.,5.],[5.,5.,5.,5.,5.]])
wynik = matrix_wlasne(a)
print(np.round(wynik,decimals=3), sep = "\n")