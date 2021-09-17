m =int(input('m = '))
n =int(input('n = '))

matrix =[]
for i in range(m):
    a =[]
    for j in range(n):
        a.append(i)
    matrix.append(a)
for i in range(m):
    print(*matrix[i])