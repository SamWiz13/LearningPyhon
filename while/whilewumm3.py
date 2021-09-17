from math import *
n = float(input("n ="))
i =1; s=0
while i <=n:
    s +=pow(1/(2*i+1),2)
    i +=1
print("Yig'indi: ",s)