m =int(input("M :"))
a =[[0 for  i in range(m)] for  i in range(m)]
for i in range(m):
    print(*a[i])
print("******************")

dx =0
dy =0
z =m**2
for i in range((m//2) +1):
    if i ==m//2:
        z +=1
    for j in range(dy, m -dx):
        a[dy][j] =z
        z -=1
    for i in range(dx + 1, m -dy -1):
        a[i][m -dx -1] =z
        z -= 1
    for j in range(m -dx -1, dx -1, -1):
        a[m -dy -1][j] =z
        z -=1
    for i in range(m -dy -2, dy, -1):
        a[i][dx] =z
        z -=1
    dx +=1
    dy +=1
for i in range(m):
    for j in range(m):
        print(a[i][j],end=" ")
    print()
