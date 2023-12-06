#12.	Izdelaj program ki šteje tako, da izpusti vsa števila, ki vsebujejo 3, 5 ali 7.
meja = int(input("Štej do: "))

i = 0

while i <= meja:
    if '3' not in str(i) and '5' not in str(i) and '7' not in str(i): ##preveri če število i (pretvorjeno v string) ne vsebuje števk 3,5 ali 7
        print(i)
    i += 1