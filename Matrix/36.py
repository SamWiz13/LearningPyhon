m =int(input("M :"))
n =int(input("N :"))
a =[[int(input("a :")) for i in range(n)] for j in range(m)]
for i in range(m):
    print(*a[i])

