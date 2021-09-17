n = int(input("n :"))
d =0
for i in range(1,n+1):
    j =1;s =0
    for j in range(1,i+1):
        if  i %j ==0:
            s +=1
    if  s ==2:
        d += 1
        print(j,end=" ")
print(" ")
print("Natija :",d)
