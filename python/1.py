## 1.	Izdelaj program, kjer te figura vpraša po vnosu petih števil in nato
## preveri ali so števila vnesena v naraščajočem vrstnem redu. 
## Če so, reče »Naraščajoče«, sicer reče »Zmešano«. Uporabi zanko.

prejsnjeSt = 0
narascujoca = True

for i in range(5):
    x = int(input("Vnesi " + str(i+1) + ". število: "))
    if x < prejsnjeSt:
        narascujoca = False
    prejsnjeSt = x
    

if narascujoca:
    print("Števila so naraščujoča.")
else:
    print("Števila so zmešana.")


#Napisal MM