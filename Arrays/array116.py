from  random import  randint
n =int(input("N :"))
a =[randint(1,8) for i in range(n)]
print(a)
b =[]
c =[]
s =1
for i in range(1,len(a)):
    if a[i-1] ==a[i]:
        s +=1
    else:
        b.append(a[i-1])
        c.append(s)
        s =1
b.append(a[len(a)-1])
c.append(s)
print(b)
print(c)

