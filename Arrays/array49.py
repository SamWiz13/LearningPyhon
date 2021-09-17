from random import  randint
n =int(input("N :"))
a =[randint(-2*n,2*n) for i in range(n)]
print(a)
x =False
for i in range(len(a)):
    if  a[i] <1 or a[i] > n:
        print(a[i], end=" ")
        print("index :", i)
        x =True
if x:
    pass
else:
    print(0)