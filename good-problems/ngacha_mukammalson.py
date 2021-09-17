n =int(input("n :"))
for i in range(1,n+1):
    s=i;k=0
    for j in range(1,s+1):
        if s %i ==0:
           s +=1
if k ==2:
    print(s)
