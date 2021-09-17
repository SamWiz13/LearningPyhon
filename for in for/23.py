n = int(input("n :"))
s=0
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        s += 1
        print(s,end=" ")
    print()
