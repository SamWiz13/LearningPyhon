n =int(input("N :"))
d =1
i =0
while i <=n:
    d *=(4*i+1)/(2*(2*i+1))
    i +=1
print(d)