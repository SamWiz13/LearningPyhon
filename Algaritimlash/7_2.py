n =int(input("n :"))
f =1
s =0
for i in range(1,n+1):
    f *=i
    s +=f**2/(2**(i**2))
print(s)