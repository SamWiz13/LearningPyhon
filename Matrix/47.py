from  random import  randint
m =int(input("M :"))
n =int(input("N :"))
a =[[randint(1,10) for i in range(n)] for  j in range(m)]
for i in a:
    print(*i)

k1 =int(input("k1 :"))
k2 =int(input("k2 :"))
a[k1],a[k2]=a[k2],a[k1]
for i in a:
    print(*i)
