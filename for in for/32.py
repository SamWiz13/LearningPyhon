n=int(input("n="))
for i in range(0,n):
    k=i; r=0
    for j in range(i,n+i):
        if k!=0:
            print(k,end=" ")
            k-=1
        else:
            print(r,end=" ")
            r+=1
    print()