from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
maxi =max(a)
mini =min(a)
for i in range(n):
    if a[i] ==maxi:
        a[i] =mini
    elif a[i] ==mini:
        a[i] =maxi
print(a)
