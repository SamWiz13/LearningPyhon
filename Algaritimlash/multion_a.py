n =int(input("N :"))
d =1
i =1
while i <=n:
    d *=i/(3-i+i*i)
    i +=1
print(d)