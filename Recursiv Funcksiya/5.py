def fib2(n):
    global k
    if n <= k:
        return d[n]
    d[n] = fib2(n - 1) + fib2(n - 2)
    k = n
    return d[n]

d = [1] * 20
k = 1
a, b, c = map(int, input().split())
print(fib2(a))
print(fib2(b))
print(fib2(c))