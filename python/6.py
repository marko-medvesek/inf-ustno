#6.	Izdelaj program, ki prešteje število soglasnikov v besedi, ki jo uporabnik vnese.

beseda = input("Vnesi besedo: ")
stSoglasnikov = 0

for crka in range(len(beseda)): ## za vsako črko v besedi
    if beseda[crka] in 'bcčdfghjklmnprsštvzžćđxy':
        stSoglasnikov += 1

print("Število soglasnikov je " + str(stSoglasnikov))

#Napisal MM