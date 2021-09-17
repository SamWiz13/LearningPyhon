a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
if  ((a > b) and (b > c) or (c > b) and(b > a)):
 print("b", " middle  number")
elif ((b > c) and (c > a) or (a > c) and (c > b)):
 print("c", " middle number")
elif ((c > a) and (a >b) or (b > a) and (a > c)):
 print("a", " middle number")
