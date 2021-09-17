n =int(input("n :"))
i=3;j=1
print(2, end=" ")
while j<n:
    for k in range(2,i):
        if i%k==0:
            break
    if  i ==k+1:
        print(i,end=" ")
        j +=1
    i +=1


