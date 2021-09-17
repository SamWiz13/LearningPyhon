from random import randint
n =int(input("N :"))
a =[randint(1,8) for i in range(n)]
print(a)

k =int(input("k :"))
b =[]
c =[]
s =1

for i in range(1,len(a)):
    if a[i-1]==a[i]:
        s +=1
    else:
        b.append(a[i-1])
        c.append(s)
        s =1
b.append(a[len(a)-1])
c.append(s)

a=[]
for i in range(len(b)):
    if k==i+1:
        c[i]*=2
    for j in range(c[i]):
        a.append(b[i])
print(a)