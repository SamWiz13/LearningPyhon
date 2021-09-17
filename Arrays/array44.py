from  random import  randint
a=[randint(1,10) for i in range(10)]
k=0;i=1
print(a,)
while k<len(a):
    son=a[k]
    for i in range(len(a)):
        if a[i] ==a[k]:
            i +=1
            print(a[k],end=" ")
    k +=1
print(i)



