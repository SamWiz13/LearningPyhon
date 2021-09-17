from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for  i in range(n)]
print(a)
i=0
while i < len(a):
    k =a.count(a[i])
    s =a[i]
    while 3>k >0:
        a.remove(s)
        k -=1
    i +=1
print(a)