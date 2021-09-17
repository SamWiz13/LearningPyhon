from  random import  randint
n =int(input("N :"))
r =int(input("R :"))
if n >0:
    a =[randint(1,10) for i in range(n)]
    print(a)
    x =True
    for i in range(1,n):
        if x:
          mini =a[i-1] +a[i]
          b =[i-1]
          s = a[i]
          x =False
        if r > a[i-1] +a[i]:
            b =a[i-1]
            s =a[i]
            mini =a[i-1] +a[i]
    print(b,end=" ")
    print(s)
else:
    print("R 1 dan katta bolshi kerak")
