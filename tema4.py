#Avand lista de mai jos.Folositi un for ca sa iterati prin toata lista si sa afisati
#1a) Masina mea preferata este x’

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    print(f'Masina mea preferata este: {masini [x]}')

#2b Faceti acelasi lucru cu un for each
for masina in masini:
    print(f'Masina mea preferata este {masina}')

#3b Faceti acelasi lucru cu un while
x = 0
while x <= len(masini)-1:
    x+=1
    print(f'Masina mea preferata este: {masini[x-1]}')

# 2.Aceeasi lista Folositi un for In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(1, len(masini)-1):
    masini[x] = masini[x].upper()
print(masini)

#3. Aceeasi lista,
#Vine un cumparator care doreste sa cumpere un Mercedes
#Iterati prin ea prin for each
#Daca masina e mercedes (if)
#Printam ‘am gasit masina dorita de dvs’
#Iesim din ciclu folosind un cuvant cheie care face acest lucrua
#Printam Am gasit masina X. Mai cautam

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    if masini[x] == 'Mercedes':
        print(f'Am gasit masina dorita de dvs:', masini[x])
        break
    else:
        print(f'Am gasit masina,', masini[x], '. Mai cautam')

#4.Aceasi lista
#Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
#Daca masina e Trabant sau Lastun
#Folositi un cuvant cheie care sa dea skip la ce urmeaza
#Printati S-ar putea sa va placa masina x

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    if (masini[x]=='Trabant' or masini[x]== 'Lastun'):
        continue
    print(f'S-ar putea sa va placa masina', masini[x])
#5.Modernizati parcul de masini
#Creati o lista goala, masini_vechi
#Iterati prin masini
#Cand gasiti Lastun sau Trabant:
#Salvati aceste masini in masini_vechi
#uprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
#Printati Modele vechi: x
#Modele noi: x

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for x in range(len(masini)):
    if (masini[x] == 'Trabant' or masini[x] == 'Lastun'):
        masini_vechi.append(masini[x])
        masini[x]  = 'Tesla'
masini=list(set(masini))
print(f'Modele vechi:',masini_vechi)
print(f'Modele noi:', masini)

#6. Avand dict
# pret_masini =
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

pret_masini = {'Dacia': 6800,'Lastun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
for x,y in pret_masini.items():
    if y <= 15000:
       print(x,y)
       print(f'Pentru un buget de sub 15000 euro puteti alege masina {x,y}')

#7.
# Avand lista
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x=0
for i in numere:
   if i==3:
       x+=1
print(x)
# 8.Aceeasi lista
# iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s = 0
for numar in numere:
    s = s + numar
print(f'Suma este',{s})

# 9.Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

s = numere[0]
for numar in numere:
    if s < numar:
        s= numar
print(s)

# 10.Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numar_nou = []
for x in numere:
    if x>0:
        x=-x
    numar_nou.append(x)
print(numar_nou)



