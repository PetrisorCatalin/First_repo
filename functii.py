def printGreeting():
    print("Buna ziua! Bine ati venit!")


# zona de apelare (desktop)
printGreeting()
printGreeting()

def printGreetingbyname (nume, prenume):
    print(f'Buna ziua {nume}, {prenume}')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def pivalue ():
    return(3.14)

#exerctitiu daca persoana este majora sau nu
def verificaremajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

printGreetingbyname( 'petrisor' , 'catalin')
printGreetingbyname( 'petrisor' , 'camelia')
printGreetingbyname( 'petrisor' , 'sebastian')
print(mediaNr(2,3,10))
print(pivalue())
print(verificaremajor(18))

#se ia varsta utilizatorului

age = int(input('Introduceti varsta dvs'))
if verificaremajor(age):
    print('Felicitari cont creat, Bine ati venit')
else:
    print('Ne pare rau nu indepliniti varsta necesara pt a putea crea contul dvs')
