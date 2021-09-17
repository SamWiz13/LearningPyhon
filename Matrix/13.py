from  random import  randint
m =int(input("m :"))
a =[[randint(1,9) for  i in range(m)] for  j in range(m)]
for i in range(m):
    print(*a[i])

mat =[]
for i in range(m):
    ong =[]
    for j in range(m):
        if j ==m-1 or i ==m-1:
            ong.append(0)
    mat.append(ong)
for i in range(m):
    print(*mat[i])