#11.	Napiši program, ki te vpraša po dveh številih in potem našteje vsa soda števila med njima.

a = int((input("Vnesi število a: ")))
b = int((input("Vnesi število b: ")))

if a > b:
    for i in range(1,a-b):
        if (b+i) % 2 == 0:
            print(b+i)
else: ## b > a
    for i in range(1,b-a):
        if (a+i) % 2 == 0:
            print(a+i)

#Napisal MM