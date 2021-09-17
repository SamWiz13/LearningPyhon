from random import randint
n =int(input("N :"))
x =[randint(-10,10) for i in range(n)]
y =[randint(-10,10) for i in range(n)]
print(x)
print(y)

r =True
for i in range(len(x)):
    if r:
        maxi =(x[i]**2 + y[i]**2)**0.5
        j =i
        r =False
    if maxi  < (x[i]**2 + y[i]**2)**0.5:
        maxi =(x[i]**2 + y[i]**2)**0.5
        j=i
print(x[i],y[i])