from  random import  randint
n=int(input('N :'))
k=int(input('K :'))
h=int(input('h :'))
a=[randint(1,10) for i in range(n)]
print(a)
a=a[:k+1]+a[h-1:k:-1]+a[h:]
print(a)