n = int(input("n ="))
i =1
while i <= n:
    j=1; s =0
    while j <= i:
        if i % j ==0:
           s +=1
        j +=1
    if  s ==2:
        print(i,end=" ")
    i +=1
