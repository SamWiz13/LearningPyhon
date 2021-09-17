from math import  sqrt
x1 = int(input("x1 :"))
y1 = int(input("y1 :"))
x2 = int(input("x2 :"))
y2 = int(input("y2 :"))
x3 = int(input("x3 :"))
y3 = int(input("y3 :"))
a = sqrt(pow(x2-x1,2)+pow(y2-y1,2))
b = sqrt(pow(x3-x2,2)+pow(y3-y2,2))
c = sqrt(pow(x3-x1,2)+pow(y3-y1,2))
p =(a+b+c)/2
print("P :",p)
print("S :", sqrt(p*(p-a)*(p-b)*(p-c)))