from math import *
n = float(input("n ="))
x = float(input("x ="))
i =1; s=1; f=1
while i <=n:
    s *=(1 + sin(i*x)/f)
    i +=1
    f *=i
print("Ko'paytma: ",s)