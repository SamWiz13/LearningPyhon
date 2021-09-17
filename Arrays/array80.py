from random import randint
n=int(input("N :"))
a=[randint(1,10) for i in range(n)]
print(a)
a =a[-1:-n-1:-1]
for i in range(n-1,0,-1):
    a[i]=a[i-1]
a.pop(i)
a.append(0)
print(a)

