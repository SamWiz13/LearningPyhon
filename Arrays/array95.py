from  random import  randint
n =int(input("N :"))
a =[int(input("a :")) for i in range(n)]
print(a)
for i in range(1,n):
    if a[i-1] ==a[i]:
        a.pop(i-1)
    print(a)



