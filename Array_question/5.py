from  random import  randint
n =int(input("N :"))
m =[randint(1,10) for i in range(n)]
v =[randint(1,10) for j in range(n)]
print(m)
print(v)

x =True
for i in range(n):
    if x:
        maxi =m[i]/v[i]
        j =i
        x =False
    if maxi <m[i]/v[i]:
        maxi =m[i]/v[i]
        j =i
print("Max :",m[j]/v[j])
print("Index :",j)