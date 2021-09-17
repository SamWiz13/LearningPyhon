from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)

k =int(input("k :"))
a =a[k+1:n]+a[:k+1]
print(a)