from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9)for i in range(n)]for j in range(m)]
for i in a:
    print(*i)
print()

for i in range(m//2):
    # for j in range(n):
        a[i],a[i+m//2]=a[i+m//2],a[i]

for i in a:
    print(*i)
