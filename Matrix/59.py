from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9)for i in range(n)]for j in range(m)]
for i in a:
    print(*i)
print()

for i in range(m):
        a[i],a[m-1]=a[m-1],a[i]
for i in a:
    print(*i)