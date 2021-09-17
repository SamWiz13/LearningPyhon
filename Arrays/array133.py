from random import randint
n =int(input("N :"))
x =[randint(-10,10) for i in range(n)]
y =[randint(-10,10) for i in range(n)]
print(x)
print(y)

r =True
for i in range(len(x)):
    if x[i]<0 and y[i]>0  or x[i] <0 and y[i]<0 and r:
        maxi =(x[i]**2+y[i]**2)**0.5
        j =i
        r =False
    if maxi < (x[i]**2+y[i]**2)**0.5 and x[i] <0 and y[i] >0 or x[i] <0 and y[i] <0:
        maxi =(x[i]**2+y[i]**2)**0.5
        j =i
print(x[j],y[j])