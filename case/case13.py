from  math import *
lm = input("Lm :")
if  lm =="a":
    a = float(input("a :"))
    print("c =",a*sqrt(2))
    print("h =",a*sqrt(2)/2)
    print("s =",a*a/2)
if lm =="c":
    c = float(input("c :"))
    print("a =",c/sqrt(2))
    print("h =",c/2)
    print("s =",c*c/4)
if lm =="h":
    h = float(input("h ="))
    print("a =",2*h/sqrt(2))
    print("c =",2*h)
    print("s =",h*h)
if lm =="s":
    s = float(input("s :"))
    print("a =",sqrt(2*s))
    print("c =",sqrt(4*s))
    print("h =",sqrt(s))