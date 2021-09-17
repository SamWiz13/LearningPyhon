n = int(input("O'inlik sanoq sistemasida: "))
s=0; k =0
while n>0:
    a = n %8
    n //=8
    s +=a*10**k
    k+=1
print(s)