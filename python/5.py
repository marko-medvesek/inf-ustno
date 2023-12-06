## 5.	Izdelaj program, ki te vpraša po vnosu štirih števil
## in ti potem pove eno izmed števil, ki ni najmanjše. Uporabi zanko.

#za število, ki ni najmanjše sem izbral kar največje število

najvecje = 0

for i in range(4):
    x = int(input("Vnesi " + str(i+1) + ". število: "))
    if x > najvecje:
        najvecje = x

print("Število, ki ni najmanjše je: " + str(najvecje))

#Napisal MM