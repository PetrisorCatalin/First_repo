#1. Functie care sa calculeze si sa returneze suma a 2 numere
import math


def suma (a,b):
    print(a+b)
suma(10,20)
suma(2,9)
#2.Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def par_impar(x):
    if x%2==0:
        print (True)
    else:
        print(False)
par_impar(4)
par_impar(7)
#3.Functie care returneaza numarul total de caractere din numele tau complet.
#(nume, prenume, nume_mijlociu)
def lungime(n):
    n = input("Scrieti Nume si Prenume ")
    print(f'Nr total de caractere {len(n)}')

lungime('PetrisorCatalinMarian')
#4. Funcție care returnează aria dreptunghiului

def aria_dreptunghi(x,y):
    print(f'Aria dreptunghi este {x*y}')

aria_dreptunghi(7,5)
aria_dreptunghi(8,25)
#5.Funcție care returnează aria cercului
def aria_cerc(r):
    print(f'Aria cercului este {math.pi*r*r}')
aria_cerc(8)
#6.Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu

def find(x):
    y = input("Scrieti textul dorit")
    if x in y:
        print(True)
    else:
        print(False)
find("a")
find("b")
#7.  Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y
def nr_caractere_dupa_case(string):
    lower = 0
    upper = 0
    for x in string :
        if x.islower():
            lower += 1
        if x.isupper():
            upper += 1
    print(f'Nr de caractere lower case este {lower}')
    print(f'Nr de caractere upper case este {upper}')



#8.Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
numere = [3,4,7,8,10,1,-5,-2,-1]
def pozitive(numere):
    x=0
    while(x<len(numere)):
        if numere[x]>0:
            print(numere[x])
            x+=1

pozitive(numere)

# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
def numbers(x,y):
    if x > y:
        print(f'Primul nr {x}, este mai mare decat al doilea {y}')
    elif x < y:
        print(f'Al doilea nr {y}, este mai mare decat primul {x}')
    else:
        print(f'Numerele {x} si {y} sunt egale')

numbers(10,10)

# #10.Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
def numar (numar,set) :
    is_in_set = numar in set
    if is_in_set :
        print('nu am adaugat numarul in set. Acesta exista deja')
    else:
        set.add(numar)
        print('am adaugat numarul nou in set')
    return is_in_set




