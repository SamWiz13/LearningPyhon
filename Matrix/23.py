from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])

for i in range(m):
    for j in range(n):
        print(i," min ",min(a[i]))
        break

