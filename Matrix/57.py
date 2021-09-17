from  random import  randint
m =int(input("M :"))
n =int(input("N :"))
a =[[randint(1,9) for i in range(n)] for j in range(m)]
for i in a:
    print(*i)
print()

for i in range(m//2):
    for j in range(n//2):
        a[i][j],a[i+m//2][j+n//2] =a[i+m//2][j+n//2],a[i][j]
for i in a:
    print(*i)