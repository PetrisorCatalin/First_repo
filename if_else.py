piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par printam acest lucru
# atfel printam impar
nr = 3
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

#este un nr pozitiv?
if (nr > 5):
    print('pozitiv')
else:
    print('nr nu este pozitiv')

# if, else if, else

# cum ne saluta robotelul in functie de ora
# luam date de la tastatura si ne asiguram ca sunt transformate din string in int
# ora = int(input('Introdu ora'))
# if ora < 0:
#     print('ora negativa')
# elif ora <= 11:
#     print('buna dimineata')
# elif ora <= 18:
#     print('Buna ziua')
# elif ora <= 21:
#     print('Buna seara')
# elif ora <= 24:
#     print('Noapte Buna')
# else:
#     print('ora mai mare decat 24')
# CTRL + / ( cu aceasta comanda poti comenta sau decomenta o rulare a unui cod! selectezi si apesi CTRL = /

# Ex Robotel telefonic

optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales romana')
elif optiunea == 2:
    print('ati ales engleza')
else: print('nu am identificat optiunea, mai incearca')