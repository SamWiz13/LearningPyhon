from  random import  randint
m =int(input("M :"))
n =int(input("N :"))
a =[[randint(-10,10) for i in range(n)] for  j in range(m)]
for i in a:
    print(*i)