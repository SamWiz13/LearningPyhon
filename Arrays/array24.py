n =int(input("N :"))
a =[int(input("a :")) for i in range(n)]
print(a)
for i in range(n):
    d =a[i] - a[i-1]
print(d)