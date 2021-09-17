n =int(input("N :"))
a=[]
for i in range(n+1):
    a.append(i)
a[1]=0
sana =0
m =2
while m <n:
    if a[m] !=0:
        j =m*2
        while j <n:
            a[j] =0
            j +=m
            sana +=1
    m +=1
for i in range(2,n):
    if a[i] !=0:
        print(a[i],end=" ")
print()
print(sana)

