'''
exercitii cu string
'''

# text = 'Ana are mere si pere, si vrea sa le manance pe toate'
# print("lungimea este", len(text))
# print(len(str(12345)))
#
# nume = input("Numele meu este")
# print("nume")

#metode string
# text = 'ana are mere'
# print(text.upper()) #capitalizeaza variabila mea
# print(text.count('e'))# numara litera e de cate ori apare in text
# print(text.index('mere'))
# print(text*10)

#operatori

numar = 10
numar = numar +12
numar += 1
numar *= 12 #valoare de dinainte se inmulteste cu 10 (10+12+1)*10
numar /= 2
print(numar**2) #numar la puterea a 2 a
assert 5 > 3
assert 5>= 3
assert 5==5
assert 5!=6
numar = 15
print(numar)
print( 20<numar<30)

# #if - daca
# nota_examen = 4
# if nota_examen >=5 :
#     print('alina a trecut examenul')
# else:
#     print('alina a picat!mai invata')
# numar = int(input("Da-mi un numar"))
# if 6%3==0:
#     print(f'{numar} se imparte la 3')
# else:
#     print(f'{numar} nu se imparte la 3')

optiunea = int(input('optiunea ta este'))
if optiunea == 0 :
    print('ati ales limba romana')
elif optiunea == 1:
    print('ati ales lb franceza')
else:
    print('ati ales o limba ce nu exista')


