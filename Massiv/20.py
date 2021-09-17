from  random import randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
for i in range(len(a)-1):
       a[i],a[i+1] =a[i],a[i+1]
print(a)