#8.	Napiši program, ki našteje vse trimestne večkratnike podanega števila.

x = int(input("Vnesi število: "))

rezultat = 0
i = 1

while rezultat < 1000: ##ponavlja zanko dokler ne pride do 1000, kar ni več trimestno število
    rezultat = x * i #pomnoži število x z i
    i += 1 #poveča i za 1
    if 100 <= rezultat < 1000: ##če je rezultat večji od 99 in hkrati manjši od 1000
        print(rezultat)