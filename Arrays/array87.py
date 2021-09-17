from random import  randint
n =int(input("N :"))
a=[randint(1,20) for i in range(n)]
print(a)
print(a[0],end=" ")
b =a[1:]
print(sorted(b))