n = int(input("n ="))
a = 0
s=0
t = False
while n >0:
     a = n % 10
     n  //=10
     if a % 2 == 1:
         t = True
         break
if t:
 print("Bor")
else:
 print("Yo'q")
