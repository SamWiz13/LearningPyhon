n =int(input("n :"))
a=[2,1]

for i in range(2,n):
    a =a[0:1]+a[1:n:]
print(a)
print(sum(a))
