from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])
x =[]
for i in range(m):
    b =[];c =0
    for j in range(1,n,2):
        b.append(a[i][j])
        c +=1
    x.append(b)

print("********************")
for i in range(m):
    print(x[i]," Sum :",sum(x[i])/c)
