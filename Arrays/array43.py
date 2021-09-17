from  random import  randint
n =int(input("N :"))
a =[randint(1,100) for i in range(n)]
print(a)
sana=0
for i in range(len(a)-1):
    if (a[i] > a[i+1] and a[i] > a[i-1]) or (a[i] < a[i+1] and a[i] < a[i-1]):
        sana +=1
        print(a[i],end=" ")
print()
print("Soni: ",sana)
