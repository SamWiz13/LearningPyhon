from  random import  randint
m =int(input("m :"))
a =[[randint(1,9)for i in range(m)]for j in range(m)]
for i in a:
    print(*i)

for i in range(m):
    s =0
    for j in range(m):
        if i ==j:
           s +=a[i][j]
    print(s)