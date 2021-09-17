from random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
print(a[::2])
b =a[::2]
mini =min(a[::2])
res =[]
for j in range(0,len(b)):
    if mini ==b[j]:
        res.append(j)
print(str(res))


