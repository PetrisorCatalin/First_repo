class Elev:
    #atribute,(fields)
    nume = ""
    prenume = ""
    cod_matricol = ""
    note = []

    #constructor
    #cand facem clasa/obiect si vrem sa le punem niste caracteristici le punem intr-un constructor
    def __init__(self, nume, prenume, cod_matricol):
        self.nume = nume
        self.prenume = prenume
        self.cod_matricol = cod_matricol

    def descrie_elev(self):
        print(f'Ma numesc {self.nume} {self.prenume} si am cod matricol {self.cod_matricol}')

elev = Elev("Ion", "BArbu", "25585")
print(elev.prenume)
elev.descrie_elev()
