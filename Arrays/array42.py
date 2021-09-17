from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
print(a)
x=True
r =int(input("R :"))
for i in range(1,len(a)-1):
     if x:
        mini =abs(r-a[i] + a[i+1])
        b,c =a[i],a[i+1]
        x =False
     if mini > abs(r-(a[i] + a[i+1])):
        mini =abs(r-(a[i] + a[i+1]))
        b,c =a[i],a[i+1]
print(b,c)
