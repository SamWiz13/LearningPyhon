from  random import  randint
n =int(input("N :"))
a =[randint(-10,10) for  i in range(n)]
print(a)

i =0
while i <len(a):
    if a[i]<0:
        a.insert(i+1,0)
    i +=1
print(a)
