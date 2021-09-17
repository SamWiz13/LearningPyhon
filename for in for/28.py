n = int(input("n :"))
for i in range(0,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(" ",end="")
    for k in range(0,2*i-1):
        print("*",end="")
    print()
