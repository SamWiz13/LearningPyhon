from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)
s =0
for i in range(len(a)):
    if a[i] %2 ==0:
        b =a[i]
        s +=1
        print(b,end=" ")
print()
print("Soni :",s)
