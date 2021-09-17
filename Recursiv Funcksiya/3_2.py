def powern(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 /powern(x, -n)
    else:
        if n % 2 == 0:
            return powern(x, n // 2) **2
        else:
            return x *powern(x, n - 1)

x = int(input("x = "))
n1, n2, n3 = map(int, input().split())
print(powern(x, n1))
print(powern(x, n2))
print(powern(x, n3))
