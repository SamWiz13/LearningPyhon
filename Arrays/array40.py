from random import randint
n=int(input("N :"))
r=int(input("R :"))
if n > 0:
    x =True
    a =[randint(-10,10) for i in range(n)]
    print(a)
    for i in range(1,n):
        if x:
            mini =abs(a[i-1]-r)
            closer =a[i-1]
            x =False
        if mini > abs(a[i]-r):
            closer =a[i]
            mini =abs(a[i]-r)
    print(closer)
else:
    print("n eng kamida 1 bo'lishi kerak")
