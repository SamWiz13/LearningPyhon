n= int(input("n :"))
for i in range(n,0,-1):
    for j in range(1,n+1):
        if  i ==j:
            print(1,end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if  i ==j:
            print(1,end=" ")
        else:
            print(" ",end=" ")
    print()
