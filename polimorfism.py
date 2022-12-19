def adunare(a,b,c=0, d=1):
    return a + b + c + d

print(adunare(3,4,5,9))
print(adunare(3,4))
print(adunare(2,3,4,))

class Bird:
    def describe(self):
        print("i am a bird")
    def fly(self):
        print("i can fly")

class Papagal(Bird):
    def vorbeste(self):
        print("i can speak")
#daca avem 2 merode cu nume identice una in clasa parinte si una in clasa copil se apeleaza aia din clasa copil
class Pinguin(Bird):
    def fly(self):
        print("Nu pot zbura")

pingu = Pinguin()
pingu.fly()
coco = Papagal()
coco.fly()
