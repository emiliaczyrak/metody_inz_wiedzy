from numpy import true_divide

print('e' in "emi")

for i in range(21):
    print(i)


def splituj(text,param):
    pomoc = ""
    tablica = []
    for letter in text:
        if letter != param:
            pomoc+=letter
        else:
            tablica.append(pomoc)
            pomoc =""
    if(pomoc!=''):
        tablica.append(pomoc)
    print(tablica)
   
splituj("Emilia Czyrak Emi Hehe Lol", " ")

def haslo(haslo):
    upper = 0
    special = 0
    for letter in haslo:
        if letter.isupper():
            upper +=1
        if letter=='!':
            special+=1

    if len(haslo) > 10 and upper>0 and special>0:
        return True 
    else:
        return False

print(haslo('emi12!eeEe122!!!!'))

lista = [1,2,99,3,4]

def wypisz(lista):
    for elem in lista:
        if elem == 99:
            continue
        print(elem)
wypisz(lista)

def czyNalezy(elem, lista):
    i=0
    help = False
    while i < len(lista):
        if elem == lista[i]:
            help = True
        i+=1
        return help
print(czyNalezy("em", ["lol", "emi", "uwm"]))


lines = []
with open('./lab02/data.txt') as f:
    lines = f.readlines()

for line in lines:
    print(f'{line}', end="") 
