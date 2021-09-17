from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)

i =0
while i <len(a):
    if a[i] % 2 ==1:
        a.insert(i,a[i])
        i +=1
    i +=1
print(a)