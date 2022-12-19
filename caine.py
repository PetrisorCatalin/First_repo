class Caine:
    rasa = ""
    greutate = ""
    varsta = ""
    sex = ""
    culoare = ""
    stapan = ""
    are_pedigree = False

    def __init__(self, rasa, varsta, sex):
        self.rasa = rasa
        self.varsta = varsta
        self.sex = sex

    def descrie(self):
        print(f'Cainele meu e de rasa {self.rasa}, are {self.varsta} si e {self.sex}')

    def varsta_in_ani_omenesti(self):
        return self.varsta*7

    def la_multi_ani(self):
        self.varsta = self.varsta+1

    def a_fost_cumparat(self, stapan):
        self.stapan = stapan

spark = Caine('LABRADOR', 5, "MASCUL")
spark.descrie()
spark.culoare = 'negru'
print(spark.culoare)
print(spark.varsta_in_ani_omenesti())
