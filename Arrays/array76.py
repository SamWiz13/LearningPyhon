from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
b=a.copy()
for i in range(1,n-1):
    if a[i] > a[i+1] and a[i] >a[i-1]:
        b[i] =0
a =b.copy()
del b
print(b)