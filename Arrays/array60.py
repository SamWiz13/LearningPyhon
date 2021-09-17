from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
b =[sum(a[i:]) for i in range(n)]
print(b)

