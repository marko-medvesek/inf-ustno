#19.	Napiši program, ki tvori aritmetično zaporedje a, a + d, a + 2d, a + 3d, …, 
#       tako da te na začetku vpraša po a in d.

a = int(input("Vnesi število a: "))
d = int(input("Vnesi število d: "))
n = int(input("Koliko števil želiš: "))

for i in range(n):
    print(a+(i*d))

#Napisal MM