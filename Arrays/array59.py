from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
b =[sum(a[:n])/n]
print(b)
