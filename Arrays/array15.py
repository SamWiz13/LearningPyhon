from random import  randint
n =int(input("N :"))
while n %2 !=0:
    n =int(input("n juft son emas: "))
a =[randint(1,10) for i in range(n)]
print(a)
a =a[1::2] + a[n-2::-2]
print(a)