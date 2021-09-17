from random import randint
n = int(input("N :"))
a = [randint(1, 10) for i in range(n)]
print(a)
a = a[n-1:] +a[0:n]
print(a)
