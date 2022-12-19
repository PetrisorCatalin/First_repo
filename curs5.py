lista = [1, 2, -4, 7, 5, 8, 9, -5]
for i in range(0, len(lista)): # e interval deschis la capat
     # ''' i o sa fie pe rand valoarea 0,1,2,3....7'''
    if lista[i] > 0:
        lista[i] = -1*lista[i]
print(lista)