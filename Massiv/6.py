from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
a.sort()
print(a)
print(a[-1:-n-1:-1])
