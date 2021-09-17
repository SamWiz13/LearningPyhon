n =int(input("n :"))
f =1
s =0
for i in range(1,n+1):
    f *=(i+1)
    s +=(2**(i+1)*(i**3 +1))/f
print(s)