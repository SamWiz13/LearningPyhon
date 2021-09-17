k = int(input("K :"))
a1=1;a2=2
for i in range(3,k+1):
    ak=(a1+2*a2)/3
    a1=a2
    a2=ak
    print(ak)