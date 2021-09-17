from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])

x =[]
for i in range(n):
    b =[]
    for j in range(m):
        b.append(a[j][0::2])
    x.append(b)
for i in range(n):
    print(*x[i])