from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
maxi =max(a)
mini =min(a)
for i in range(n):
        if  a[i] < maxi and a[i] >mini:
            a[i]=0
print(a)
