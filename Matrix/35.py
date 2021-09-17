from  random import randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,10) for i in range(n)] for j in range(m)]
for i in a:
    print(*i)

for i in range(n):
    for j in range(m):
        k =j
        print(a[i][k],end=' ')
        break