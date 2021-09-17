from random import  randint
m =int(input("M :"))
n =int(input("N :"))
a =[[randint(1,9) for  i in range(n)] for  j in range(m)]
for i in range(m):
    print(*a[i])
arr =[]
for i in range(m):
    b=[]; s=0
    for j in range(n):
        s +=a[i][j]
    print(s)