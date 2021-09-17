from  random import  randint
n =int(input("N :"))
a =[randint(1,100) for i in range(n)]
print(a)

x =True
s =[]
for i in range(1,len(a)-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        s.append(a[i])
    if a[i] > a[i-1] and a[i] > a[i+1] and x:
        maxi =a[i]
        x =False
    if a[i] > a[i-1] and a[i] > a[i+1] and maxi < a[i]:
        maxi =a[i]
print(s)
print(maxi)
