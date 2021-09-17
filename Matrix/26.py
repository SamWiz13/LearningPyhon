from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(-9,9) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])
x =True
for i in range(n):
    b =[];mini =1
    for j in range(m):
        if x:
            mini *=a[j][i]
            k=j
            u =i
            x =False
        if mini >a[j][i]:
            mini =a[j][i]
            k =j
            u =i
    b.append(a[k][u])
print(b)
