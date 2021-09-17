from  random import  randint
m =int(input('m = '))
n =int(input('n = '))
a=[[randint(1,9) for j in range(n)] for i in range(m)]
for i in  range(m):
    print(*a[i])
k =int(input('k = '))

for i in  a:
    print(a[k])
    break


