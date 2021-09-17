from random import randint
n =int(input("N :"))
k =int(input("k :"))
l =int(input("l :"))
a =[randint(1,10) for i in range(n+1)]
print(a)
print(a[:k] + a[l+1:])
print(round((sum(a[k:])+sum(a[l+1:]))/(n-(l-k+1))))