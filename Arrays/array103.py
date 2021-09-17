from random import  randint
n =int(input("N :"))
a =[randint(0,20) for i in range(n)]
print(a)

x =True
for i in range(n):
    if x:
        maxi =a[i]
        mini =a[i]
        j =i
        k=i
        x =False
    if maxi <a[i]:
        maxi =a[i]
        j =i
    if mini >a[i]:
        mini =a[i]
        k =i
a.insert(j+1,0)
a.insert(k,0)
print(a)

