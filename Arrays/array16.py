from random import randint

n=int(input("N="))
a=[]
b=[]
a=[randint(0,n) for i in range(n)]
print(a)
b.extend(a)
b.reverse()
print("Natija:",end=" ")

t=n//2
if n%2!=0:
    t+=1
for i in range(t):
    print(a[i],b[i],end=" ")
