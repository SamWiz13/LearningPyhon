from random import randint
n=int(input('n = '))
while n%2!=0:
    n=int(input('N juft emas yana kiriting = '))
a=[randint(1,10) for i in range(n)]
print(a)

a=a[1::2]+a[n-2::-2]
print(a)