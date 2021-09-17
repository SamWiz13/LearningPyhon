from  random import  randint
n =int(input("N :"))
a =[randint(1,100) for i in range(n)]
b =[randint(1,100) for i in range(n)]
print(a)
print(b)
P =2*(max(a)+max(b))
print("Eng katta  perimetr :",P)