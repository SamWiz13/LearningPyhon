n = int(input("n ="))
c =1
sana =0
while c <=n:
    b =1
    while b <c:
        a = 1
        while a <b:
            sana +=1
            if  c*c == a*a + b*b:
                print(c,b,a)
            a +=1
        b +=1
    c +=1
print("Sikl soni: ",sana)