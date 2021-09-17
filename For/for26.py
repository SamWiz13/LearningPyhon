n = int(input("n :"))
x = int(input("x :"))
s =0
for i in range(1,2*n+2,2):
    s +=(x**i)/i
    x *=-1
print(s)
