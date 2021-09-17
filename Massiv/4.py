from random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
maxi =max(a)
mini =min(a)
print("Max :",maxi)
print("Mini :",mini)
print("Separation :",maxi -mini)