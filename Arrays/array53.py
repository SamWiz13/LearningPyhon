from  random import randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
b =[randint(1,10) for i in range(n)]
print(a)
print(b)
c =[max(a[i],b[i]) for i in range(n)]
print("C :",c)
