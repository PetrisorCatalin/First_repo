#liste
# o lista poate pastra diferite tipuri de date in aceeasi lista
lista = ["ioana", "Maria", 56, 123.5,True, False,[1,2,3,4], ["mazda", "dacia"]]
print(lista[2]) #indexul dintr-0 lista incepe cu numaratoarea de la 0
print(len(lista))
print(lista[len(lista)-1])
#se pot modifica, putem sterge elemente, putem adauga elemente, putem schimba valorile, putem duplica
print(lista[5:])
index = lista.index(True)
print(lista[index])
#cum adaugam
lista.append("tema")
print(lista)
import random
random_index = random.randint(0, len(lista)-1)
print(lista[random_index])

#set "{zodiac, culori, animale etc...}"
#Are doar valori unice
#nu sunt ordonate sau indexate
#nu putem schimba locatia elementelor, nu putem insera
#putem adauga si sterge
# se poate folosi len

culori = {"alb", "rosu", "verde"}
culori.remove("verde")
print(culori)
#print(culori.pop(1))

#tuple
#valorile au index, incep de la 0
#nu putem adauga sau sterge
#accepta valori duplicate
#se poate folosi len
#nu se pot suprascrie

fructe = ("mere", "banane", "pere")
print(fructe[0])

#dictionar
#sunt mutabile valorile pot fi suprascrise, putem adauga si sterge
#cheile sunt unice
# date de tip cheie de valoare
# se poate folosi len
dict = {"ion":4, "vasile":6, "maria":9}
carduri =  {"brd":1234, "otp":2345}
masina = {"brand":"dacia", "model":"Spring", "year":2020, "automata":True}

#afisam valoarea unei cheie
print(dict["ion"])
print(masina.get("model"))
#asa suprascriem
masina["brand"] = "MAzda"
print(masina)
#asa adaugam
masina["cai putere"]= 100
print(masina)
#asa sterg
masina.pop("year")
print(masina)
if "tema" in lista:
    print()