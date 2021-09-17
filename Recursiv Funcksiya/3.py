n =int(input("n daraja:"))
x =int(input("x :"))
def Power(x,n):
    if n %2 ==0 or n >0:
        return (x**(n/2))**2
    elif n %2 ==1 or n >0:
        return (x**n)*(x**(n-1))
    else:
        return 1/(x**(-n))
print(Power(x,n))




