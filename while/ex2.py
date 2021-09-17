n = int(input("n ="))
i =1; s =0
while i <=n:
    if  n % i ==0:
        print(i,end=" ")
        s +=i
    i +=1
print(" ")
print("Yig'indi: ",s)