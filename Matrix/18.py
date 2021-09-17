from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])

k =int(input("k :"))
for i in range(n):
    s =0;d =1
    for j in range(m):
        s +=a[j][k]
        d *=a[j][k]
print("Sum :",s)
print("Mult :",d)