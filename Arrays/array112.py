from random import  randint
n =int(input("N :"))
a=[randint(1,20) for i in range(n)]
print(a)

for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            a[i],a[j] =a[j],a[i]
print(a)