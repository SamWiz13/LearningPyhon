from random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
b =a
a =[i for i in a if i % 2==0]
b =[i for i in b if i % 2 ==1]
print(a +b)