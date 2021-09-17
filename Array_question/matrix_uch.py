n =int(input("n :"))
b =[]
for i in range(n):
    a =[]
    for j in range(n):
        if i <=j and i+j<=n-1:
            a.append(1)
        else:
            a.append(0)
    b.append(a)
for i in range(n):
    print(*b[i])