#16.	Izdelaj program, kjer uporabnik vnese besedo, figura pa jo prebere v nasprotni smeri.
# Npr. »strela« -> »alerts«

beseda = input("Vnesi besedo: ")

for i in range(len(beseda)):
    print(beseda[len(beseda)-i-1])


## način z negativnim indeksom
""" for i in range(1,len(beseda)+1):
    print(beseda[-i]) """