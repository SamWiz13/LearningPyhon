n = int(input("n :"))
s=0
for i in range(2,n+1):
    for j in range(2,i):
        if  i %j ==0:
            s = 1
            break
    if s==0:
       k=i
    s=0
print(k)

