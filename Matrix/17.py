from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])

k =int(input("k :"))
for i in range(m):
    s =0;d =1
    for j in range(n):
        s +=a[k][j]
        d *=a[k][j]
print("Sum :",s)
print("Mult :",d)

