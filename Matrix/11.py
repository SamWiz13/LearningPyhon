from  random import  randint
m = int(input('m = '))
n = int(input('n = '))
a = [[randint(1, 10) for j in range(n)] for i in range(m)]
for i in range(m):
    print(*a[i])

b = []
for i in range(n):
    c = []
    if i % 2 == 0:
        for j in range(m):
            c.append(a[i][j])
    else:
        for j in range(m - 1, -1, -1):
            c.append(a[i][j])
    b.append(c)
print()

for i in range(m):
    for j in range(n):
        print(b[i][j], end=' ')
    print()