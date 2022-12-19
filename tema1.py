# 1.În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă
# R: o variabila este o zona din memorie care tine anumite date,
# ( ne ajuta sa presetam sau sa predefinim anumite valori)

# 2.Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:
# R: varibila (tip date)  string:
echipa_fotbal = 'CFR'
# tip date integer
an_infiintare = 1907
# tip date Float
nr_spectatori = 200.100
# tip date Boolean
campioana = True
# 3.Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat
print(type(echipa_fotbal))
print(type(an_infiintare))
print(type(nr_spectatori))
print(type(campioana))
# 4. Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere), apoi verifică din nou tipul de date al acesteia.
nr_spectatori = round(nr_spectatori)
print(type(nr_spectatori))
# 5.Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin orice modalitate dorești (type casting, printare cu formatare).

print(f'Tin cu echipa {echipa_fotbal}')
print(f'Aceasta echipa a fost infiintata in {an_infiintare}')
print(f'La ultimul meci au fost in tribuna {nr_spectatori} spectatori')
print(f'Aceasta echipa este campioana Romaniei, {campioana}!')
# 6.Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'

nume = 'Petrisor'
prenume = 'Catalin'
print(f'Numele meu complet are {len(nume + prenume)} caractere')

# 7.Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.

lungime_dreptunghi = 50
latime_dreptungi = 70
print(f'Aria dreptunghiului este {lungime_dreptunghi * latime_dreptungi}')

# 8.Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare cuvântul 'the' în acest string;
# Atentie! Nu luati in considerare string-ul “the” din cuvantul “either”

coral = 'Coral is either the stupidest animal or the smartest rock'
either = 1
print(coral.count('the') - (either))

# 9.Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul

string = coral
print(string.replace('the','THE'))

# 10. Folosindu-te de string-ul de la exercițiul 8 foloseste un assert ca să verifici dacă acest string conține doar numere.

if string.isnumeric() == False:
    print(f'Fraza coral'  ' Nu contine numere')


