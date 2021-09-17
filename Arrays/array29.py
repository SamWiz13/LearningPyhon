from random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
print(a[1::2])
b =a[1::2]
maxi =max(a[1::2])
res =[]
for j in range(0,len(b)):
    if maxi ==b[j]:
        res.append(j)
print(str(res))