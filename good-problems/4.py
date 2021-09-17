n = int(input("n ="))
i=1;s=0
while i <=n:
     s +=n%10
     n //=10
print(s)
