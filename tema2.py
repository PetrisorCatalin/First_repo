# 1.Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
#R: Cu ajutorul if else putem controla anumite conditionari ale tipurilor de date folosite precum si ceea ce vrem sa executam dintr-un cod.

# 2.Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
# (conditia IF/Else)
val_x = 3
if val_x >= 0:
   print(f'{val_x} ' "ESTE NUMAR NATURAL")
else:
    print(f'{val_x} ' "Nu este numar natural")

# 3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
# (conditia if;elif;else)
if val_x == 0:
    print(f'{val_x} ' "Este numar neutru")
elif val_x < 0:
    print(f'{val_x}) ' "Este numar negativ")
else:
    print(f'{val_x}) '"Este numar pozitiv")

# 4.Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

if val_x >= -2 and val_x <= 13:
    print(f'{val_x} ' " Se afla in intervalul -2 si 13")
else:
    print(f'{val_x} ' "Nu se afla in intervalul -2 si 13")

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
   #(diferenta inseamna cate numere sunt intre x si y, nu rezultatul
   # diferentei intre x si y). Hint: Se va folosi functia abs

val_y =int(input("Introduceti valoarea lui y: "))
diferenta = val_x - val_y
print(diferenta)
if diferenta < 5:
    print( 'Diferenta dintre val_x si val_y este mai mica decat 5')
else:
    print('Diferenta dintre val_x si val_y nu este mai mica decat 5')

# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

if not 5 <= val_x <= 27:
    print(f'{val_x} '  " Nu se afla intre 5 si 17")
else:
    print(f'{val_x} ' "Se afla in intervalul 5 si 27")

# 7.Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare

val_y = int(input("Alege valoare y: "))
if val_x==val_y:
    print("Numerele au valoare egala")
elif val_x > val_y:
    print("Valoarea lui X este mai mare ")
else:
    print("Valoarea lui Y este mai mare ")

# 8.Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi,
# afiseaza daca triunghiul este isoscel (doua laturi sunt egale),
# echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala)

# cum fac sa creez inputul x y z ca sa introduc val de la tastatura pt fiecare in parte
val_x = int(input(3))
val_y = int(input(2))
val_z = int(input(2))
if val_x==val_y==val_z:
    print("Triunghiul este echilateral")
elif val_z == val_x or val_x==val_y or val_y==val_z:
    print("Triunghiul este isoscel")
else:
    print("Triunghiul este oarecare")

#9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

vocala = input("Introduce o litera: ")
vocale = ("A", "E", "I", 'O', "U", "a", "e","i","o","u")
if vocala in vocale:
    print("Litera este o vocala")
else:
    print("Litera NU este o vocala")

#10.
# Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = float(input("Introdu nota pt a afla calificativul: "))
if nota >=9 :
    print("A")
elif nota >=8:
    print("B")
elif nota >=7:
    print("C")
elif nota >=6:
    print("D")
elif nota >4:
    print("E")
else:
    print("F")

