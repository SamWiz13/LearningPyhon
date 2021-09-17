from random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
a=[i for i in a if i % 2==1]
b=a.copy()
for i in range(len(b)):
    k =b[i]
    a.insert(i,k)
print(a)