n =int(input("n :"))
def Fact(a):
    if a ==1 or a <=4:
        return 1
    else:
        return a*(a-2)*Fact(a-4)
print(Fact(n))
