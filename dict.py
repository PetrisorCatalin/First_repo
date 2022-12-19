#declaram si initializam un dict

note_elevi = {"Gigel": 10, "Costel": 9, "Ana": 10};

#adaugam elemente
note_elevi['Sebi'] = 7

#printam dictul
print(note_elevi)

#aflam elemente
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

#actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

#aflam dimensiune
print(len(note_elevi))

#sterg valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', "nu mai avem acest elev"))
print(note_elevi)

#afiseaza doar cheile
print(note_elevi.keys())