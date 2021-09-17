from math import *
n = float(input("n ="))
x = float(input("x ="))
i =1; s=0; f=1
while i <=n:
    s +=(x + cos(i*x))/pow(2,i)
    i +=1
    f *=i
print("Yig'indi: ",s)

