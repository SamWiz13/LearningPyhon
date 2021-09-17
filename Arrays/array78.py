from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
b =[]
for i in range(len(a)-1):
    b =int((a[i] +a[i+1])/n)
    print(b,end=" ")
