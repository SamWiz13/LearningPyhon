from random import randint
n=int(input("N :"))
if n>1:
    k=0
    sana=0
    a=[randint(1,10) for i in range(n)]
    print(a)
    for i in range(1,n):
        if a[i] < a[i-1]:
            if k==0:
                sana+=1
            k=1
        else:
            k=0
    print(sana)
else:
    print("n>1 sharti bajarilishi kerak")
