from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
b =max(a)
c =min(a)
for i in range(n):
    if a[i] ==b:
        a[i] =c
    elif a[i] ==c:
        a[i] =b
print(a)

