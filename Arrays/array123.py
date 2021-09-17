from random import randint
n =int(input("N :"))
a =[randint(1,4) for i in range(n)]
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

if not k >len(b):
    b[k-1],b[0]=b[0],b[k-1]
    c[k-1],c[0]=c[0],c[k-1]

a =[]
for i in range(len(b)):
    for j in range(c[i]):
        a.append(b[i])
print(a)