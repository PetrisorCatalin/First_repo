# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
#1
# Clasa Cerc
# Atribute: raza, culoare
# Constructor pt ambele atribute
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

import math
class Cerc:
    raza = " "
    culoarea = " "
    def __init__(self,raza,culoare):
            self.raza=raza
            self.culoare=culoare

    def descrie_cerc(self):
            print(f"Raza este {self.raza} si culoarea {self.culoare}")

    def aria(self,raza):
            print(math.pi*raza**2)
    def diametru(self,raza):
            print(2*raza)
    def circumferinta(self,raza):
            print(2*math.pi*raza)

cerc1 = Cerc(5, "blue")
cerc1.descrie_cerc()
cerc1.aria(5)
cerc1.diametru(5)
cerc1.circumferinta(5)
#2.
# Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:
    lungime = " "
    latime = " "
    culoare = " "

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Lungimea este {self.lungime}, latimea este {self.latime}, iar culoarea este {self.culoare}')

    def aria(self, lungime, latime):
        print(lungime*latime)
    def perimetru(self, lungime, latime):
        print(2*(lungime*latime))
    def schimba_culoarea(self, culoare):
        self.culoare = culoare

dreptunghi1 = Dreptunghi(5,8,"verde")
dreptunghi1.descrie_dreptunghi()
dreptunghi1.aria(5,8)
dreptunghi1.perimetru(5,8)
dreptunghi1.schimba_culoarea('rosu')
dreptunghi1.descrie_dreptunghi()

#3 Clasa Angajat

# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Angajat:
    nume = " "
    prenume = " "
    salariu = " "

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie_Angajat(self):
        print(f'{self.nume} {self.prenume} are salariul {self.salariu}')
    def nume_complet(self):
        print(f'Numele complet este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariu lunar este {self.salariu}')
    def salariu_anual(self):
        print(f'Salariul anual este {12 *self.salariu}')
    def marire_salariu(self,procent):
        print(f'Angajatul {self.nume} {self.prenume} are o marire de {procent}%')

angajat1 = Angajat("Petrisor", "Catalin", "5000")
angajat1.descrie_Angajat()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(10)
