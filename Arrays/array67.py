from  random import randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
x =False
for i in range(n):
    if a[i] % 2==1:
        c =a[i]
        b =a[i]+c
        print(b,end=" ")
        x =True
if x :
    pass
else:
    print(a)        