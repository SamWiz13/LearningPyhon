a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

if  (a < b < c) or (a > b >c):
    a *=2
    b *=2
    c *=2
else:
     a *=-1
     b *=-1
     c *=-1
print("a =",a)
print("b =",b)
print("c =",c)
