n = int(input("n :"))
for  i in range(1,n+1):
    s=0
    for j in range(1,i+1):
        if  i % j ==0:
            s +=1
    if  s==0:
        print(j,end=" ")
