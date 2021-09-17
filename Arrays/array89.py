n =int(input("N :"))
a =[int(input("a :")) for i in range(n)]
print(a)
for i in range(1,n-1):
    if a[i] >a[i-1] and a[i] < a[i+1] or a[i] >a[i+1]:
       a.sort()
print(a)