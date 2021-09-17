n =int(input("N :"))
a =[]
for i in range(n):
    b =[]
    for j in range(n):
        if i ==j:
            b.append(2)
        elif i > j and i + j > n - 1:
            b.append(1)
        else:
            b.append(0)
    a.append(b)
for i in range(n):
    print(*a[i])
