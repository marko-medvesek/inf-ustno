#20.	Napiši program, ki tvori geometrijsko zaporedje, a, a*q, a*q*q, 
#tako da te na začetku vpraša po vrednostih a in q.

a = int(input("Vnesi število a: "))
q = int(input("Vnesi število q: "))
n = int(input("Koliko števil želiš: "))

for i in range(n):
    print(a*(q**i))