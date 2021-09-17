def isPalindrom(n):
   i=n; r=0
   while n>0:
       d=n%10
       r=r*10+d
       n //=10
   if i==r:
        return True
   else:
        return False

n =int(input("n :"))
print(isPalindrom(n))