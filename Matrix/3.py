m =int(input('m = '))
n =int(input('n = '))

matrix =[]
for i in range(n):
    a =[]
    for j in range(m):
        a.append(j)
    matrix.append(a)
for i in range(n):
    print(*matrix[i])
