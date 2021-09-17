a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
s1=0;s2=0
while a >=c:
    s1 += 1
    a -=c
    while b >=c:
        s2 += 1
        b -=c
s3 =0
while s1 >0:
    s3 +=s2
    s1 -=1
print(s3)