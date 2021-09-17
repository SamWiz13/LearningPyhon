from  random import randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
b =[randint(1,10) for i in range(n)]
print(a)
print(b)
a,b=b,a
print("Next a:",a)
print("Next b :",b)