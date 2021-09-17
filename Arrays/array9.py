n =int(input("n :"))
a =[i for i in range(1,n+1)]
print(a)
b =[]
for i in a:
    if i %2 ==0:
        b.append(i)
print(b)
