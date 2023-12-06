## 2.	Izdelaj program, ki te vpraša po vnosu petih števil
## in ti potem pove, katero je največje. Uporabi zanko.

i = 1
meja = 5
najvecje = 0 ##dosedanje največje število

while i <= meja:
    x = int(input("Vnesi " + str(i) + ". število: "))
    if x > najvecje:
        najvecje = x
    i += 1

print("Najvecje število je bilo: " + str(najvecje))


#Napisal MM