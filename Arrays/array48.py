from  random import  randint
n=int(input("N :"))
a=[randint(1,10) for i in range(n)]
x=True
print(a)
for i in range(n):
    if x:
        k=a.count(a[i])
        x=False
    if k<a.count(a[i]):
        k=a.count(a[i])
print(k)