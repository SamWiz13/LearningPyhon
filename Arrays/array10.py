from random import  random
n =int(input("n :"))
a =[i for i in range(1,10+1)]
print(a)
b=[];c=[]
for i in a:
    if i %2 ==0:
        b.append(i)
    if i %2 ==1:
        c.append(i)
print(b,c[-1::-1])
