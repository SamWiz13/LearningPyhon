n = int(input("n ="))
x = True
while n>2:
    if  2*(n // 2) ==n:
        n //=2
    else:
        x = False
        break
if  x:
    print("Daraja")
else:
    print("Daraja emas")