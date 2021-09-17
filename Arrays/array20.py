from random import randint
n =int(input("N :"))
k =int(input("k :"))
l =int(input("l :"))
a =[randint(1,10) for i in range(n+1)]
print(a)
print(a[k:l+1])
print(sum(a[k:l+1]))
