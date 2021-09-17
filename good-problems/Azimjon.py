n = int(input(' n = '))
t = [1] * (2*n - 1)
m =[int(input('m = ')) for i in range(2*n - 1)]
if len(set(m)) == n:
    h = list(set(m))
    for i in range(n):
        t[i+n-1] = h[i]
    for i in range(n-2,-1,-1):
        t[i] = min(t[2*i + 1],t[2*i + 2])
    print("YES")
    print(t)
else:
    print("NO")

