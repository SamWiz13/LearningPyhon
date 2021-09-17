a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
if  ((a > b) and (b > c) or (c > b) and (b > a) ):
 print("a"," katta son")
 print("c", " kichik son")
elif ((b > c) and (c > a) or (a > c) and (c > b)):
 print("b"," katta son")
 print("a", " kichik son")
elif ((c > a) and (a >b) or (b > a) and (a > c)):
    print("c", " katta son")
    print("b", " kichik son")