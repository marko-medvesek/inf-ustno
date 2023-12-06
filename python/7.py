#7.	Izdelaj program, ki izpisuje potence števila, dokler ne preseže podanega števila.
# Npr., če mu uporabnik vnese2 in 10, našteje 2, 4, 8.

meja = int(input("Vnesi zgornjo mejo: "))
osnova = int(input("Vnesi osnovo potence: "))
rezultat = 0
i = 0

while rezultat <= meja:
    rezultat = osnova**i
    if rezultat <= meja:
        print(rezultat)
    i += 1

#Napisal MM