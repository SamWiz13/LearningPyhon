'''n =int(input("n :"))
x =True
for i in range(1,n+1):
    a =int(input("a :"))
    if x:
        maxi =a
        x =False
    if maxi <a:
        maxi=a
print(maxi)'''


from  random import  randint
n =int(input("n :"))
a =[randint(1,100) for i in range(n)]
print(a)
print(max(a))

