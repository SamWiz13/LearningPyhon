from  random import  randint
m =int(input("M :"))
n =int(input("N :"))
a =[[int(input("a :")) for i in range(n)] for j in range(m)]
for i in a:
    print(*i)

for j in range(n):
    maxi =a[0][j]
    k =0
    for i in range(m):
        if maxi <a[i][j]:
            maxi =a[i][j]
            k =i
    if maxi ==min(a[k]):
       print(maxi,a[k])
       break
