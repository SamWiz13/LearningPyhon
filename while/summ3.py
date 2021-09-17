n = float(input("n ="))
i =1; s=0;f =1
while i <=n:
    s +=1/f
    i +=1
    f *=i
print(s)