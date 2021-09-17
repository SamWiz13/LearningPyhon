from  random import  randint
m =int(input("m :"))
n =int(input("n :"))
a =[[randint(1,9)for i in range(n)]for j in range(m)]
for i in a:
    print(*i)
print()

for i in range(len(a)):
    for j in range(i,len(a)):
        a[i][j],a[j][i]=a[j][i],a[i][j]
N =len(a)
for i in range(N//2):
    for j in range(N):
        a[i][j],a[N-1-i][N-1-j]=a[N-1-i][N-1-j],a[i][j]

for i in a:
    print(*i)