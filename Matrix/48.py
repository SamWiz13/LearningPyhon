from  random import  randint
m =int(input("M :"))
n =int(input("N :"))
a =[[randint(1,10) for i in range(n)] for  j in range(m)]
for i in a:
    print(*i)
k1 =int(input("k1 :"))
k2 =int(input("k2 :"))
for i  in range(len(a)):
    a[i][k1],a[i][k2]=a[i][k2],a[i][k1]
for i in a:
    print(*i)