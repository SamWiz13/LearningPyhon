n =int(input("n :"))
a =[]
for i in range(1,n+1):
    b =[]
    for j in range(n,0,-1):
        if i ==j:
            b.append(i)
        else:
            b.append(0)
    a.append(b)
for i in range(n):
    print(*a[i])