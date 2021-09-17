from  random import randint
m =int(input("M :"))
n =int(input("N :"))
a =[[randint(-10,10) for i in range(n)] for j in range(m)]
for i in a:
    print(*i)

for i in range(n):
    s1 =0;s2 =0
    for j in range(m):
        if a[i][j] <0:
            s1 +=1
        if a[i][j] >0:
            s2 +=1
    if s1 ==s2:
        print(a[j])
        break

else:
    print("Bunday ustun yoq.")