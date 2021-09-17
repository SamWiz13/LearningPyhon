from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
for i in range(n):
    b =a[round(n/2):]+a[:round(n/2)]
print(b)