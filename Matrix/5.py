from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
d =int(input("d :"))
k =[randint(1,20) for i in range(m)]
print(k)

matrix =[]
for i in range(m):
    a =[];p =0
    for  j in range(n):
        a.append(k[i]+p)
        p += d
    matrix.append(a)


for i in range(m):
    print(*matrix[i])
