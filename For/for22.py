n =int(input("n ="))
x = int(input("x ="))
f =1;s =1
for i in range (1,n +1):
    f *=i
    s +=x**i/f
print("Yig'indi :",s)
