k = int(input("K :"))
f1=1;f2=1
for i in range(3,k+1):
    fk=f1+f2
    f1=f2
    f2=fk
    print(fk)