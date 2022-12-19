'''
Operatori:
aritmetici: +, -, *, /, %
de comparare: < >, ==, !=, >=, <=
logici: and, or, !
'''
a = 3
b = 5

print(a+b) # 3 + 5 => 8 (operatori aritmetici)



print(a == b) # a este egal cu b => False (operatori de comparare)



print(a < b and a < 4 ) # True SI True => True (operatori logici)
# pt ca rezultatul sa fi fost false trb ca una din conditii sa fi fost de ex a < 2 ceea ce era False
# iar rezultatul generat ar fi fost False
print(a < b or a < 2) # True SAU False => True pt ca in conditia 'or'/SAU avem una din conditii adevarate
#deci rezultatul va genera True

#cu mama sau tata sau (cu bunicu si bunica)
mama = True
tata = False
bunicu = False
bunica = False
print(mama or tata or(bunicu and bunica))