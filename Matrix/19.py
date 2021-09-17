from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])

for i in range(m):
    s =0
    for j in range(n):
        s +=a[i][j]
    print("Sum ",i," rows", s)