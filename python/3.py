## 3.	Izdelaj program, ki te vpraša po vnosu štirih števil in 
## ti potem pove, katero je najmanjše. Uporabi zanko.

meja = 5 ## število števil
najmanjse = 0 ## dosedanje najmanjse število
i = 2

najmanjse = int(input("Vnesi 1. število: "))

while i <= meja:
    x = int(input("Vnesi " + str(i) + ". število: "))
    if x < najmanjse:
        najmanjse = x
    i += 1

print("Najmanjse število je bilo: " + str(najmanjse))


#Napisal MM