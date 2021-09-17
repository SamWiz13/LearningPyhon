from random import  randint
n =int(input("N :"))
a =[randint(1,100) for i in range(n)]
print(a)
for i in range(1,len(a)-1):
    if  a[i] > a[i+1]:
        print(a[i], end=" ")

    