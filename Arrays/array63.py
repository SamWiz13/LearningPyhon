n =int(input("N :"))
a =[int(input("a :")) for i in range(n)]
b =[int(input("b :")) for i in range(n)]
c =a[:] + b[:]
print(c)
