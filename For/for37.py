n = int(input("N :"))
s =0
for i in range(1,n+1):
    a = 1
    for j in range(1,i+1):
        a *=i
        s +=a
        print(s)