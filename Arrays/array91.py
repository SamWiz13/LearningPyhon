from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
k =int(input("k :"))
m =int(input("m :"))
a =a[:k]+a[m:]
print(a)
