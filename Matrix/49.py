from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9)for i in range(n)]for j in range(m)]
for i in a:
    print(*i)
print()

x = True
for i in range(m):
        if x:
            mini =maxi =a[i]
            d =k =i
            x =False
        if maxi <a[i]:
            maxi =a[i]
            k =i
        if mini >a[i]:
            mini =a[i]
            d =i
        a[d],a[k] =a[k],a[d]

for i in a:
    print(*i)