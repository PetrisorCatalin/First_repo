"""Functii cu un parametru, 2 parametru, functii care returneaza ceva"""

# functie care nu returneaza ceva

def say_hello():
    print("Hello")

say_hello()
# functie care returneaza ceva(avem o lista si schimbam toate elementele in litere mari)
def lista_nume_capitalize(lista_nume):
    for i in range(len(lista_nume)):
        lista_nume[i] = lista_nume[i].capitalize()
    print(lista_nume)

lista_nume = ["ion", "vasile"]
lista_nume_capitalize(lista_nume)
lista_nume_capitalize(["unu", "doi", "trei"])
lista_nume_capitalize(["unu", "doi", "trei","cinci"])

#functie care sa imi zica cate zile are luna aleasa
def get_days(month):
    days_30 = ["aprilie", "iunie", "septembrie","noiembrie"]
    days_31 = ["ianuarie", "martie", "mai", "iulie", "octombrie", "decembrie"]
    if month in days_30:
        return 30
    elif month in days_31:
        return 31
    else:
        return 29
print(f'Aprilie are {get_days("aprilie")} zile')

