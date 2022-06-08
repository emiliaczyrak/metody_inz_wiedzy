# def zamien(number):
#     return float(number)
# with open('./lab03/australian.dat',"r") as file:
#     matrix = []
#     for line in file:
#         line = line.replace("\n","").split(" ")
#         line = map(zamien, line)
#         matrix.append(list(line))


# for i in range (5):
#     print(matrix[i])

import math
import numpy as np
import random as rand
with open('./lab03/australian.dat',"r") as file:
    matrix = []
    for line in file:
        line = line.replace("\n","").split(" ")
        matrix.append(list(map(lambda e: float(e), line)))


for i in range (5):
    print(matrix[i])

def euk(list1, list2):
    wynik=0
    for i in range(len(list1)):
        wynik+=(list1[i] - list2[i]) ** 2
    return math.sqrt(wynik)

print("\n -----metryka 1: ")       
print(euk(matrix[0], matrix[1]))
# print(euk(matrix[0], matrix[2]))
# print(euk(matrix[0], matrix[3]))

def euk2(list1, list2):
    v1 = np.array(list1)
    v2 = np.array(list2)
    a = v2 - v1
    return math.sqrt(np.dot(a,a))

print("-----porownanie metryk------")
print(euk2(matrix[0], matrix[1])==euk2(matrix[0], matrix[1]))

# y = lista[0]
# d(y,x) gdzie x nalezy do lista, bez elementu z indexem 0, odleglosc miedzy 0 a pozostalymi
# [] : [   ] <= [] klasa decyzyzyjna X, [   ] <= lista odleglosci  lista slownikow
# czyli jak klasa 1 - to wszystkie odleglosci z klasa 0
# napisac funkcje, ktora bedzie liczyla wyznacznik macierzy kwadratowej

def group_aust(lista,ind):
    grupy = dict()
    y = lista[0]
    for x in range(1,len(lista)):
        decyzyjna = lista[x][ind]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(euk(y, lista[x]))
        else:
            grupy[decyzyjna]=[euk(y, lista[x])]
    return grupy

print("----------- group: ---------")
print(group_aust(matrix,14))

def k_sasiad(lista,y):
    grupy = dict()
    for x in range(0,len(lista)):
        decyzyjna = lista[x][-1]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(euk(y, lista[x]))
        else:
            grupy[decyzyjna]=[euk(y, lista[x])]      
    return grupy
print("----------- 2 -------------")
print(k_sasiad(matrix, [1,1,1,1,1,1,1,1,1,1,1,1,1,1]))


# def g(x,lista):
#     D={}
#     for para in lista:
#         c = para[0]
#         if c not in D: 
#             D[c] = []
#         D[c].append(para[i])
#     return D
# print(g(matrix, [1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

def sasiad_lista(lista,nowa_osoba):
    grupy = []
    for x in range(0,len(lista)):
        decyzyjna = lista[x][-1]
        grupy.append((decyzyjna,euk(nowa_osoba, lista[x])))    
    return grupy

grupowanie = k_sasiad(matrix, [1,1,1,1,1,1,1,1,1,1,1,1,1,1])
grupowanie[0].sort()
print(sum(grupowanie[1][:5]))

def grupujemy(lista,k):
    grupy = dict()
    for element in lista:
        decyzyjna = element[0]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(element[1])
        else:
            grupy[decyzyjna]=[element[1]] 
    for klucz in grupy.keys():
        grupy[klucz].sort()
    for klucz in grupy.keys():
        suma = 0
        for ele in grupy[klucz][:k]:
            suma+= ele
        grupy[klucz]=suma
    return grupy
            
groups = grupujemy(sasiad_lista(matrix, [1,1,1,1,1,1,1,1,1,1,1,1,1,1]),5)
print(groups[0])

def decision(slownik):
    keys = list(slownik.keys())
    ilosc = 1
    klasa = keys[0]
    minimum = slownik[keys[0]]
    for key in keys[1:]:
        if minimum > slownik[key]:
            minimum = slownik[key]
            klasa = key
            ilosc=1
        elif minimum == slownik[key]:
            ilosc+=1
    if ilosc > 1:
        return 
    return klasa

print("Decyzja:",decision(groups))
print("Decyzja:",decision({0.0:4,1.0:4,2.0:3}))


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

macierz = [[1,-1,0,2],[2,1,-3,1],[3,0,0,-2],[-1,2,0,2]]
print("------- wyznacznik ----------")
print(getMatrixDeternminant(macierz))



## praca domowa:  calkowanie metoda Monte Carlo

def montecarlo(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    punkty = 1000
    ile = 0
    minimum, maximum = foo(fx), foo(lx)
    wylosowane=[]
    ile=0
    while(abs(wyliczone-oryginal)>eps):
        punkty+=1000
        for i in range(1000):
            newx = rand.uniform(fx,lx)
            newy = rand.uniform(minimum, maximum)
            while((newx,newy) in wylosowane):
                newx = rand.uniform(fx,lx)
                newy = rand.uniform(minimum, maximum)
            wylosowane.append((newx,newy))
            wynik = foo(newx)
            if(newy<=wynik):
                ile+=1
        wyliczone = (lx-fx)*(maximum-minimum)*(ile/punkty)
        print("dokladnosc: {3} ilosc {0} pkt:{1} rzeczywiste {2}".format(punkty,wyliczone,oryginal,eps))
    return wyliczone

def f2(x):
    return x**3/3

def f(x):
    return x**2

def prostokaty(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(dzielnik):
            wyliczone+= foo(fx+odleglosc*i)*odleglosc
        print("dokladnosc: {3} ilosc {0} pkt:{1} rzeczywiste {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone

def prostokaty2(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(1,dzielnik+1):
            wyliczone+= foo(fx+odleglosc*i)*odleglosc
        print("dokladnosc: {3} ilosc {0} pkt:{1} rzeczywiste {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone

def prostokaty3(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dolna = 0
    gorna = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(1,dzielnik+1):
            dolna = foo(fx+odleglosc*(i-1))*odleglosc
            gorna = foo(fx+odleglosc*i)*odleglosc
            wyliczone+= (dolna+gorna)/2
        print("dokladnosc: {3} ilosc {0} pkt:{1} rzeczywiste {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone

def srodek_masy(indeksy:list, lista:list):
    odleglosci = []
    temp_odl = 0
    for ele in indeksy:
        for ele_por in indeksy:
            temp_odl+=euk(lista[ele], lista[ele_por])
        odleglosci.append(temp_odl)
        temp_odl = 0
    mini = 0
    for i in range(1,len(odleglosci)):
        if odleglosci[mini]>odleglosci[i] :
            mini = i
    return mini
    

def nauczyciel(lista):
    grupy = dict()
    for ele in lista:
        decyzyjna = ele[14]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(ele)
        else:
            grupy[decyzyjna]=[ele]
    matrix_without_decission = [l[:14]+[float((len(grupy.keys())))] for l in lista]
    
    zmiany = True
    while(zmiany):
        zmiany = False
        grupy = dict()
        for i in range(len(matrix_without_decission)):
            decyzyjna = matrix_without_decission[i][-1]
            if decyzyjna in grupy.keys():
                grupy[decyzyjna].append(i)
            else:
                grupy[decyzyjna]=[i]
        new_matrix = []
        for ele in grupy.values():
            new_matrix+=ele
        srodki = []
        for lista in grupy.values():
            srodki.append(lista[srodek_masy(lista, matrix_without_decission)])
        odleglosci = []
        for ele in new_matrix:
            for sr in srodki:
                odleglosci.append(euk(matrix_without_decission[ele], matrix_without_decission[sr]))
            mini = 0
            ile = 1
            for i in range(1,len(odleglosci)):
                if odleglosci[mini]>odleglosci[i] :
                    mini = i
                    ile = 1
                elif odleglosci[mini]==odleglosci[i] :
                    ile=ile+1
            if ile==1 :
                if matrix_without_decission[ele][-1]!=matrix_without_decission[srodki[mini]][-1] :
                    matrix_without_decission[ele][-1]=matrix_without_decission[srodki[mini]][-1]
                    zmiany = True
            elif ile>1:
                matrix_without_decission[ele][-1]= None
                zmiany = True
            odleglosci=[]
    return matrix_without_decission
        

def matrix_roznice(m1,m2):
    ile = 0
    for i in range(len(m1)):
        if(m1[i]!=m2[i]):
            ile=ile+1
    return str((len(m1)-ile)/len(m1)*100)
    
    
new_matrix = nauczyciel(matrix)
grupy = dict()
for ele in new_matrix:
      decyzyjna = ele[14]
      if decyzyjna in grupy.keys():
          grupy[decyzyjna].append(ele)
      else:
          grupy[decyzyjna]=[ele]
for key in grupy.keys():
    print("{0}: {1}".format(key,len(grupy[key])))
print(matrix_roznice(matrix, new_matrix))


