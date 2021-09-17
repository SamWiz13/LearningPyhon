n = int(input("n ="))
s =0
i =1
while i<=n:
     s += n %10
     n //=10
print("Yig'indi: ",s)