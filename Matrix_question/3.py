n =int(input("N :"))
a =[]
for i in range(n):
    b =[]
    for j in range(n):
        if i ==j:
            b.append(n-i)
        else:
            b.append(0)
    a.append(b)
for i in range(n):
    print(*a[i])