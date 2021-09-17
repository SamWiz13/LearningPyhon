n = int(input("n :"))
a0=1
for i in range(1,n+1):
    ak =(a0+1)/i
    a0=ak
    print(ak)