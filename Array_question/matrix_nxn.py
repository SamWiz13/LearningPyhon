n =int(input("n :"))
b =[]
for i in range(n):
    a =[]
    for j in range(n):
        if i ==j or i +j ==n-1:
            a.append(0)
        elif i < j and i + j < n - 1:
            a.append(2)
        elif i < j and i + j > n - 1:
             a.append(3)
        elif i > j and i + j > n - 1:
             a.append(4)
        else:
            a.append(5)
    b.append(a)
for i in range(n):
    print(*b[i])