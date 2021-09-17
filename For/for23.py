n = int(input("n :"))
x = int(input("x :"))
s =x; f=1;a=-1
for i in range(3,2*n+1,2):
    f *=(i-1)*i
    s +=a*x**i/f
    a *=-1
print(s)