#9.	Napiši program, ki našteje vse trimestne potence podanega števila.

x = int(input("Vnesi osnovo potence: "))
if x==1:
    print("Potenca števila 1 bo vedno 1!")
    exit() ##predčasno zaključi program

rezultat = 0
i = 1

while rezultat < 1000: ## ponavljaj dokler je rezultat manjši od 1000 (ko je večji od 999 ni več trimestno število)
    rezultat = x**i
    i +=1
    if 100 <= rezultat < 1000:
        print(rezultat) 
"""     if -1000 < rezultat <= -100:  ##tako bi izgledalo če bi želeli upoštevati še  negativna števila
        print(rezultat)  """