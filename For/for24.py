n = int(input("n :"))
x = int(input("x :"))
s =1; f=1;a=-1
for i in range(2,2*n+1,2):
    f *=(i-1)*i
    s +=a*x**i/f
    a *=-1
print(s)