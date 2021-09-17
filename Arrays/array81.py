from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
k =int(input("k :"))
a=[0]*k +a[:k]
print(a)
    