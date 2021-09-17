n =int(input("N :"))
d =1
i =1
while i <=n:
    d *=(1- 1/pow(i+1,2))
    i +=1
print(d)