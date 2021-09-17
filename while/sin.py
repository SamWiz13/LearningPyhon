from  math import *
n = int(input("n ="))
i = 1;s=0;ps =0
while i <=n:
    ps +=sin(i)
    s +=1/ps
    i +=1
print(s)