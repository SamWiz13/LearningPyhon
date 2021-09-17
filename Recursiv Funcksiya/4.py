n =int(input("N :"))
def Fib(n):
    if n ==2 or n ==1:
        return 1
    else:
        return Fib(n-2)+Fib(n-1)
print(Fib(n))