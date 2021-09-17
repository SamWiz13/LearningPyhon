from random import randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in a:
    print(*i)
mat =[]
c =[]
for i in range(len(a)-2):
    b =[]
    for j in range(len(a)-2):
        if a[i][j] <a[i][j+1] and a[i][j+1]<a[i][j+2]:
            b =a.append(a[i][j+1])
    c.append(b)
mat.append(c)
for i in mat:
    print(*i)


