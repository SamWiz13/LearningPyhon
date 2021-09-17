n =int(input("N :"))
a =[i for i in range(1,n+1,2)]
b =[i for i in range(2,n+1,2)]
a.extend(b)
print(a)