from  random import  randint
n =int(input("N :"))
k =int(input("k :"))
a =[randint(1,10) for i in range(n)]
print(a)
a =[a[i]+a[k] for i in range(n)]
print(a)