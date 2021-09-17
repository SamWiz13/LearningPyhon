from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)

for i in range(len(a)-1):
    if a[i] >a[i-1]:
        print(i,end=" ")