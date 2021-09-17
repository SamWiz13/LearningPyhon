from  random import  randint
n=int(input('n = '))
a=[randint(1,20) for i in range(n)]
print(a)

for i in range(len(a)-1):
    if (a[i]*a[i+1])% 2 ==0:
        print(i+1,end=" ")
else:
    print("0")