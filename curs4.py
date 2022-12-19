# """ while, for"""
# #cat timp ceva e adevarat
# i=0
# #la while trb sa ne asiguram, ca conditia o sa fie si flasa


# incercari = 0
# pin = "1234"
# pin_introdus = input("Da-mi pinul")
# while incercari <= 2 and pin != pin_introdus:
#     print("Pinul nu e corec, mai incearca")
#     pin_introdus = input("alt pin")
#     incercari = incercari + 1
# print("Cardul e blocat sau pinul nu e corect")

#sa stergem din lista elemente daca se afla de mai multe ori in lista
# lista = ["vasile",'ion', "MAria", "Alex",'ion']
# while lista.count("ion")>1:
#     lista.remove("ion")
#     print(lista)
# #suma tuturor numerelor pare pana la 100
# i=2
# suma = 0
# while i <= 100:
#     suma += i
#     i+=2
#     print(suma)
# # pentru....executa codul din interior
#for
# suma2 = 0
# for i in range(0,101):
#     suma2 += i
# print(suma2)

#suma din 4 in 4
# for i in range(0,1006,5):
# suma2 += i
#     print(i)
# print(suma2)

lista_note = [3, 4, 6, 8, 9, 10]
suma = 0
for nota in lista_note:
    if nota == 8:
        continue
    suma += nota
print(suma/len(lista_note))

