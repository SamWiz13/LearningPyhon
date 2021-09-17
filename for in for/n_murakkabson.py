n = int(input("n :"))
x3 = True
for i in range(2,n//2+1):
    x2=False; x1 =False
    for j in range(2,i):
        if  i %j ==0:
            x1 =True
            break
    for j in range(2,n-i):
        if (n-i)%j ==0:
            x2 = True
            break
    if x1 and x2:
       print(n,"=",i,"+",n-i)
       x3 = False
if x3:
    print("Yechim yoq!")