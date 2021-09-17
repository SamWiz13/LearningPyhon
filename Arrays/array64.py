n =int(input("N :"))
a =[int(input("a :")) for i in range(n)]
b =[int(input("b :")) for i in range(n)]
c =[int(input("c :")) for i in range(n)]
d =a+b+c
print(sorted(d))