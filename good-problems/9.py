from  random import  randint
n =int(input("N :"))
a =[randint(1,20) for i in range(n)]
print(a)

maxi =max(a)
mini =min(a)
print(maxi,mini)
x =round((maxi +mini)/n)
print("Orta arifmetik:",x)
for i in range(len(a)):
    if a[i] ==x:
        print(a[i])
        break
else:
    print("Tugadi")




