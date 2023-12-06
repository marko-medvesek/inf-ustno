## 4.	Izdelaj program, ki te vpraša po vnosu štirih števil in ti potem
## pove eno izmed števil, ki ni največje. Uporabi zanko.



""" # 1. VARIANTA - vrne drugo največje število
i = 1
najvecje = 0 ##dosedanje največje število
neNajvecje = 0

while i <= meja:
    x = int(input("Vnesi " + str(i) + ". število: "))
    if x > najvecje:
        neNajvecje = najvecje ## neko število ki je bilo dosedaj največje, je sedaj drugo največje 
        najvecje = x ## vnos (x) je sedaj novo največje število
    i += 1

print("Drugo največje število je bilo: " + str(neNajvecje))
"""

meja = 4
najvecje = 0
neNajvecje = 0

for i in range(meja):
    x = int(input("Vnesi " +  str(i+1) + ". število: "))
    if x > najvecje:
        neNajvecje = najvecje
        najvecje = x
    else:
        neNajvecje = x
    
print(neNajvecje) 


#Napisal MM