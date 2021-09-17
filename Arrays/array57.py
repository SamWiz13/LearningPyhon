from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
b =a[::2]+a[1::2]
print(a)
print(b)