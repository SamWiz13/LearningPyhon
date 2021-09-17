n =int(input("N :"))
b =[int(input("b :")) for  i in range(n)]
print(b)

for i in range(n):
    q =b[i]/b[i-1]
print(q)