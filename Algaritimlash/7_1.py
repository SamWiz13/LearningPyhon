n =int(input("n :"))
f =1
s =0
for i in range(2,n+1):
    f *=(i-1)
    s  +=(i+1)/(2**i)*f
print(s)