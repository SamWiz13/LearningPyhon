n = int(input("O'nlik sanoq sistemasida :"))
s =0; k = 0
while n >0:
    a = n%2
    n //=2
    s +=a*10**k
    k +=1
print(s)
