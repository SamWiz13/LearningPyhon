from random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
maxi =max(a)
mini =min(a)
print(maxi)
print(mini)
print("Sum :",maxi +mini)