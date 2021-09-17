from random import randint
n=int(input("n="))
a=[randint(1,7) for i in range(n)]
print(a)
for i in range(n-1,0,-1):
    a[i]=a[i-1]
a[0]=0
print(a)