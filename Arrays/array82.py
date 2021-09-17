from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
k =int(input("k :"))
a=a[k+1:]+[0]*(n-1-k)
print(a)
