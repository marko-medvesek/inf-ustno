## 13.	Izdelaj program, ki pove koliko je različnih samoglasnikov v besedi, ki jo vnese uporabnik.
# Beseda »banana« ima le en samoglasnik »a«.

samoglasniki = 'aeiou'
beseda = input("Vnesi besedo: ")

for i in range(len(samoglasniki)): ##za vsak samoglasnik v nizu samoglasnikov
    if samoglasniki[i] in beseda: ##preveri če je samoglasnik v besedi
        print(samoglasniki[i]) ##ga izpiše

#Napisal MM