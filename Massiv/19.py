from  random import randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
a =[i for i in a if i %3 ==0]
print(a)