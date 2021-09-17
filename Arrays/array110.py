from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
a =[i for i in a if i % 2 ==0]
b=a.copy()
i =0
while i <len(b):
        b.insert(i,b[i])
        i +=1
        i +=1
print(b)