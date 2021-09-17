from  math import sqrt
n = int(input("n ="))
i = 2; t =True;j = sqrt(n)
while i <=j:
    if  n % i ==0:
        t = False
        break
    i +=1
if t:
 print("Tub son")
else:
 print("Tub emas")
