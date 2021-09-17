def ekub(a,b):
    if b ==0:
        return a
    else:
        return ekub(b,a%b)
a =int(input("a :"))
b,c,d =map(int, input().split())
print(ekub(a,b))
print(ekub(a,c))
print(ekub(a,d))