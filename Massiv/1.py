from  random import  randint
n =int(input("n :"))
a =[randint(1,20) for i in range(n)]
print(a)
print(sum(a)/n)
