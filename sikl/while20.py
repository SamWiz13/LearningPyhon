n = int(input("n ="))
s=0
while n >0:
    if  n % 10==2:
        s +=1
    n  //=10
print(s)