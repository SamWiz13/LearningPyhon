from random import randint
n=int(input('n = '))
k=int(input('k = '))
a=[randint(1,10) for i in range(n)]
print(a)
print("******************")
a=a[::k]
print(a)






