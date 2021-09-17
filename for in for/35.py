n = int(input("Ikkilik sanoq sistemasida :"))
s =0; k = 0
while n >0:
    a = n%10
    n //=10
    s +=a*2**k
    k +=1
print(s)