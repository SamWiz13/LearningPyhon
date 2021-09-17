def len(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**0.5

from random import randint
n =int(input("N :"))
x =[randint(-10,10) for i in range(n)]
y =[randint(-10,10) for i in range(n)]
print(x)
print(y)

c =[]
for i in range(n):
    s=0
    for j in range(n):
        s +=len(x[i],y[i],x[j],y[j])
    c.append(s)
a =c.index(min(c))
print(a)
