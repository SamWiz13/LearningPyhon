n = int(input("n :"))
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print()

