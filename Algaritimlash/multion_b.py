n =int(input("N :"))
d =1
i =2
while i <=n:
    d *=(i+1)/((i-1)*i)
    i +=1
print(d)