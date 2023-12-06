#15.	Izdelaj program, kjer uporabnik vnese neko besedilo, 
#       potem pa program pove to besedilo brez samoglasnikov.

besedilo = input("Vnesi besedilo: ")
rezultat = ''

for i in range(len(besedilo)):
    if (
        'a' not in besedilo[i].lower() and
        'e' not in besedilo[i].lower() and 
        'i' not in besedilo[i].lower() and 
        'o' not in besedilo[i].lower() and 
        'u' not in besedilo[i].lower() ):
        rezultat = rezultat + besedilo[i]

print(rezultat)

#Napisal MM