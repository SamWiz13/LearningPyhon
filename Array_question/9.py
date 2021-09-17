from  random import  randint
n =int(input("N :"))
a =[randint(1,100) for i in range(n)]
print(a)

x =True
for i in range(n):
    if x:
        maxi =a[i]
        k =j =i
        x =False
    if maxi ==a[i]:
        maxi =a[i]
        k =i
    if maxi <a[i]:
        maxi =a[i]
        j =i
print(a[k],a[j])
print(k,j)