n =int(input("N :"))
a =[int(input("a :")) for i in range(n)]
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

a=[]
maxi=c[0]
index=0
for i in range(len(c)):
    if maxi >=c[i]:
        maxi =c[i]
        index =i
c[index]+=1

for i in range(len(b)):
    k =b[i]
    for j in range(c[i]):
        a.append(k)
print(a)