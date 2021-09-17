from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
for i in range(0,n,2):
    a[i],a[i+1] =a[i+1],a[i]
print(a)