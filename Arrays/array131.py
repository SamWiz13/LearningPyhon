from random import randint
n =int(input("N :"))
x =[randint(-10,10) for i in range(n)]
y =[randint(-10,10) for i in range(n)]
print(x)
print(y)
b =int(input("b :"))

r =True
for i in range(len(x)-1):
    if r:
        maxi =((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)**0.5
        j =i
        k =i+1
        r =False
    if maxi > ((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)**0.5 and b>((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)**0.5:
        maxi =((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)**0.5
        j =i
        k =i+1
print(x[j],y[j])
print(x[k],y[k])