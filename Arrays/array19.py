from random import randint
n =int(input("N :"))
k =int(input("K :"))
a =[randint(1,n) for i in range(1,n+1)]
if a[0] < a[k] <a[-1]:
    print(a)
else:
    print(0)
