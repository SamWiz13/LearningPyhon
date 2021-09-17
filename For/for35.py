k = int(input("K :"))
a1=1; a2=2; a3=3
for i in range(4,k+1):
    ak= a3 + a2 - 2*a1
    a1=a2
    a2=a3
    a3=ak
    print(ak)