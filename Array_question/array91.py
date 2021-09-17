from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)

k =int(input("k :"))
m =int(input("m :"))

i =0
while i <m-k:
        a.pop(k+1)
        i +=1
print(a)