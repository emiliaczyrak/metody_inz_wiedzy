import math as m
import numpy as np

matrix = []
with open("./lab03/australian.dat","r") as file:
    matrix = [list(map(lambda a: float(a),line.split())) for line in file]

def srednia(lista):
    suma = 0.0
    for x in lista:
        suma+=x
    return float(suma/(float(len(lista))))

def wariancja(lista):
    srednia = srednia(lista)
    suma= 0.0
    for x in lista:
        suma+= (x - srednia)**2
    return float(suma/(float(len(lista))))

def odchylenie(lista):
    return m.sqrt(wariancja(lista))


print(srednia([1,2,3]))