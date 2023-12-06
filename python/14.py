#14.	Izdelaj program, ki te vpraša po vnosu petih števil, in ti potem pove,
# koliko od teh števil je sodih in koliko je lihih. Uporabi zanko.

stevecLih = 0
stevecSod = 0

for i in range(5):
    x = int(input("Vnesi " + str(i+1) + ". število: ")) ## i+1 je zato ker je na začetku i=0
    if (x % 2) == 0: ##za x preveri ostanek pri deljenju z 2 (sodo)
        stevecSod += 1
    else: ##v nasprotnem primeru je število liho
        stevecLih += 1
print("Sodih števil: " + str(stevecSod))
print("Lihih števil: " + str(stevecLih))

#Napisal MM