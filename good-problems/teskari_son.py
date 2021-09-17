a =int(input("a :"))
i=1
while i<=a:
    s =a%10
    a//=10
    print(s,end="")