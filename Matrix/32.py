from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(-10,10) for i in range(n)] for j in range(m)]
for i in a:
    print(*i)


for i in range(m):
    s1 =0;s2 =0
    for j in range(n):
        if a[i][j]<0:
            s1 +=1
        if a[i][j]>0:
            s2 +=1
    if s1 ==s2:
        print(a[i])
        break
else:
    print("Bunday satr yoq.")