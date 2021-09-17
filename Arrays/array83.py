from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)

a =a[-1:]+a[0:n-1]
print(a)