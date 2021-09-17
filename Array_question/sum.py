from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
b =[sum(a[n-i-1:]) for i in range(n)]
print(b)