n =int(input("n :"))
a =[int(input("a :"))]
d =int(input("d :"))

for i in range(1,n):
    a.append(a[i-1]+d)
print(a)
