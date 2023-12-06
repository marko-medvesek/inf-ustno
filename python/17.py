#17.	Izdelaj program, kjer te figura vpraša po dveh besedah enake dolžine in potem
# iz njiju ustvari novo besedo, tako da vzame prvo črko prve besede,
# nato prvo črko druge besede, nato drugo črko prve … Npr.: ris, pot -> rpiost

rezultat = ''

a = input("Vnesi 1. besedo: ")
b = input("Vnesi 2. besedo: ")

if len(a) != len(b): ##če dolžini besed nista enaki potem zatarna
    print("Dolžini besed morata biti enaki!")
    exit()##predčasno zaključi program

for i in range(len(a)):
    rezultat = rezultat + a[i] + b[i]

print(rezultat)

#Napisal MM