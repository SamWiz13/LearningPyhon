from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)

for i in range(len(a)):
    k =a[i]
    j =i
    while a[j-1] >k and j >0:
        a[i] =a[j-1]
        j -=1
    a[j] =k
print(a)

