a = int(input("a ="))
b = int(input("b ="))
if a > b:
    s = a
    a = b
    b = s
    print("a =",a, " ","b =",b)