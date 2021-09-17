from random import randint
n =int(input("N :"))
a =[]
a =[randint(1,n) for i in range(1,n+1)]
print(a)
if a[-1] >a[-2] :
    print(a[-2])
else:
    print(0)