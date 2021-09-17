from random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
k =int(input("k :"))
for i in range(n-1):
    if a[i] ==k:
        a.pop(i)
print(a)