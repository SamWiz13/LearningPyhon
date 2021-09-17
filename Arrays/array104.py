from random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
k =int(input("k :"))

for i in range(n):
    if i ==k:
        a.insert(i,0)
        print(a)
