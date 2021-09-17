n =int(input("n ="))
f =1;s =0
for i in range (1,n +1):
    f *=i
    s +=1/f
print("Yig'indi :",s)
