a = int(input("a ="))
b = int(input("b ="))
if  a !=b:
    if a >b:
        b= a
    else:
        a =b
elif a == b:
    a =0
    b =0
print("a =",a)
print("b =",b)