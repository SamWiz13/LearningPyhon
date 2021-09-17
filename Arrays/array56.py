from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
b =a[3::3]
print(b)
