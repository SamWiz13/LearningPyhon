a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
d = float(input("d ="))

if  (a ==b) and (b ==c) :
    orin =4
if ( a ==b) and (b ==d):
    orin =3
if (a ==d) and (c ==d):
    orin =2
if (b ==c ) and (c ==d):
    orin =1
if (orin == 0):
    print("Bir-biriga teng sonlar yoq")
else:
    print(orin," soni boshqalaridan fariqli.")
