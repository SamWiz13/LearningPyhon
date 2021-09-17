from random import  randint
n =int(input("N :"))
a =[randint(1,5) for i in range(n)]
print(a)
b=[randint(1,10) for i in range(n)]
for i in range(len(a)):
    if a[i] < 5:
        b[i] =2*a[i]
    else:
        b[i] =a[i] /2
print(b[i],"index :",i)
