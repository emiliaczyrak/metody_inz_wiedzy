name = "emilia"
age=22
print("mam na imie {} wiek: {}".format(name, age))

# x = input('podaj ulub liczbe: ')
# print(x)
imie = "jacek"
print(imie[::-1])

liczba = '1'
liczba2 = 2
liczba3 = 2.34

print("typ zmiennej 1: {}, typ zmiennej 2: {}, typ zmiennej 3: {}".format(type(liczba), type(liczba2), type(liczba3)))

list = ["school", "food", "sleep", "work"]
listJoin = " ".join(list)
print(listJoin)

splitek = listJoin.split()
print(splitek)

txt = "Metody Inżynierii Wiedzy są najlepsze"
print("zdanie: {} , dlugosc: {}".format(txt, len(txt)))
zmienna =  txt.replace('ą', 'a').replace('ż', 'z').replace(' ', '')
print("zdanie: {} , dlugosc: {}".format(zmienna, len(zmienna)))
zmSet = set(zmienna)
print(zmSet, len(zmSet))

zm10 = ('emi', 22)
print(type(zm10))

list1 = [1,2,3,4,5]
list2 = ['e', 'm', 'i']
list3 = list1+list2
print(list3)
print(list3[2:3], type(list3[2:3]))
print(list1.index(3))

list1.extend(list2)
print(list1)
list1.append("new")
print(list1)

disc = {'emi':22, 'pawel':21, 'wiki':22, 'konrad':22}
print(disc, type(disc))

stolice = {'Polska': 'Warszawa', 'Niemcy': 'Berlin', 'Czechy': 'Praga', 'Rosja': 'Moskwa', 'Ukraina': 'Kijow', 'Litwa':'Wilno', 'Białoruś': 'Mińsk'}
stoliceSort = {k: v for k, v in sorted(stolice.items(), key=lambda item: item[1])}
print(stoliceSort)