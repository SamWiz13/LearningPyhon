from  random import  randint
n =int(input("N :"))
a =[randint(1,8) for i in range(n)]
print(a)
k =int(input("k :"))
m =int(input("m :"))

a =a[:k+1] +[0]*m +a[k+1:]
print(a)