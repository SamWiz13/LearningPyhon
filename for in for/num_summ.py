n = int(input("n :"))
s =0
for i in range(1,n+1):
     s +=n %10
     n //=10
print("Natija :",s)