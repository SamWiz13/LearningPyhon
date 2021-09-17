from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])

for i in range(n):
    d =1
    for j in range(m):
        d *=a[j][i]
    print("Mult ",i," colums", d)