from random import randint
n =int(input("n :"))
a=[randint(1,10) for i in range(n)]
print(a)
for i in range(len(a)-1):
    if a[i]>a[i-1] and a[i] > a[i+1]:
        print(a[i],end=" ")


