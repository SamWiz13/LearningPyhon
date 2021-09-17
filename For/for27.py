n = int(input("n :"))
x = int(input("x :"))
s =x;k=1;m=1
for i in range(1,n+1,2):
    k*=(2*i-1)*i
    m*=(2*i)*(2*i+1)
    s +=x**i*k/m
print(s)