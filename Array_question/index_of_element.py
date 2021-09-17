from  random import  randint
n =int(input("N :"))
a =[randint(1,100) for i in range(n)]
print(a)
for i in range(n):
    print(i," index",a[i])
