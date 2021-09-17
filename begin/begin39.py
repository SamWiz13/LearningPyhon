from  math import sqrt
a = int(input("A :"))
b = int(input("B :"))
c = int(input("C :"))
D = b*b - 4*a*c
x1 = (-b+sqrt(D))/2*a
x2 = (-b-sqrt(D))/2*a
print("X1 :",x1)
print("X2 :",x2)
