n = int(input("n :"))
a = int(input("a :"))
s=0
for i in range(1,n+1,2):
    s+=a**i
print("Yig'indi: ",s)
