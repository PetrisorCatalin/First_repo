# variabila este o zona din memoria unui calculator care tine date
# sau o mai putem denumi ca o cutiuta de valori
# exemple mai jos de varibile (am declarat si initializat valori )
marca_masina = 'Volvo'
model_masina = 'XC 60'
# nu putem pune spatiu in numele unei variabile, daca avem cuvant de legatura punem underscore
# in python nu trebuie sa specificam tipul de date folosit ( de asta este loosely typed)
print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

#suprascriere
model_masina = 'XC 60 Facelift'

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul  : {model_masina}')

nume = 'Petrisor'
prenume = 'Catalin'
varsta = 34
print (f'{nume} {prenume} si am varsta de {varsta}')