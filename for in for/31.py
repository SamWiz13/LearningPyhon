n = int(input("n :"))
for i in range(0,n+1,):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(i-1,-i,-1):
        print(i+k,end=" ")
    print()