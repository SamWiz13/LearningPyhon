from math import *
n = float(input("n ="))
x = int(input("x = "))
i =1; s=0; f =1
while i <=n:
    s +=(pow(x,i))/f
    i +=1
    f *=i
print("Yig'indi: ",s)