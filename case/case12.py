from  math import *
lm = input("Lm :")
if  lm =="r":
    r = float(input("r :"))
    print("D =",2*r)
    print("l =",2*pi*r)
    print("s =",pi*r*r)
if lm =="d":
    d = float(input("d :"))
    print("r =",d/2)
    print("l =",pi*d)
    print("s =",pi*d*d/4)
if lm =="l":
    l = float(input("l ="))
    print("r =",l/pi*2)
    print("d =",l/pi)
    print("s =",l*r/2)
if lm =="s":
    s = float(input("s :"))
    print("r =",sqrt(s/pi))
    print("d =",sqrt(4*s/pi))
    print("l =",s*2/r)