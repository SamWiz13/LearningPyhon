n = int(input("Darajani kiriting :"))
a = int(input("Sonni kiriting :"))
s =0
for i in range(n+1):
    s +=a**i*(-1)**i
print(s)
