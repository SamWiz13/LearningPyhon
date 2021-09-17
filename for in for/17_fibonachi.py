n = int(input("n: "))
f0=0; f1 =1
for i in range(1,n+1):
    fn = f0 +f1
    f0 =f1
    f1 = fn
    print(f0,end=" ")
