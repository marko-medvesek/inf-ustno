## 18.	Izdelaj program ki iz podane besede odstrani podvojene črke. Npr. maarella -> marela.

## beseda = 'maaarellaaaaaa'
beseda = input("Vnesi besedo: ")

resitev = ''

for i in range(len(beseda)):
    
    if beseda[i] in resitev: ##Če je i-ta črka iz besede že prisotna v rešitvi potem
        
        if beseda[i-1] == beseda[i]:   ##preveri če je ta ponovljena črka zaporedna (npr. aa), tako da pogleda na prejšnji index (i-1)
            print("Črka '" + str(beseda[i]) + "' na indexu " + str(i) + " je zaporedno podvojena")
        else:
            resitev = resitev + beseda[i]

    else:
        resitev = resitev + beseda[i]

print(resitev)

#Napisal MM