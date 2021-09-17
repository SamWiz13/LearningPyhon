from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9)for i in range(n)]for j in range(m)]
for i in a:
    print(*i)
print()

for i in range(m):
     for j in range(n//2):
        a[i][j],a[i][j+n//2]=a[i][j+n//2],a[i][j]

for i in a:
    print(*i)