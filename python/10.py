#10.	Izdelaj program, ki najprej vpraša po dveh številih in nato
# našteva večkratnike prvega števila, dokler ne preseže drugega števila.

x = int(input("Vnesi število: "))
meja = int(input("Vnesi zgornjo mejo: "))

i = 1
rezultat = 0

while rezultat <= meja:
    rezultat = x*i
    i += 1
    if rezultat <= meja:
        print(rezultat)

#Napisal MM