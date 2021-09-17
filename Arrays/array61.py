from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
k =int(input("k :"))
for i in range(k,n):
    b= sum(a[i:])/i
    print(b)
    break