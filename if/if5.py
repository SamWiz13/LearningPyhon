a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
plus = 0
minus = 0
if  a >0:
    plus +=1
if b >0:
    plus +=1
if c > 0:
    plus +=1
if a < 0:
    minus +=1
if b < 0:
    minus +=1
if c < 0:
    minus  +=1
if (plus ==0):
    print("Musbat son kiritilmadi.")
else:
    print(plus, " ta musbat son kiritildi.")
if (minus == 0):
        print("Manfiy son kiritilmadi.")
else:
        print(minus, " ta manfiy son  kiritildi.")
