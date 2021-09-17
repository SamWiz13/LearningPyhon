"""
def combin(n,k):
    if k ==0 or k ==n:
        return 1
    else:
        d[n][k] =combin(n,k) +combin(n-1,k-1)
        k =n
        return d[n][k]
n =int(input("n :"))
k =int(input("k :"))
d =[1]*20
print(combin(n,k))
"""
a, b, c, n = [int(input()) for i in range(4)]
print ([[x,y,z] for x in range(a + 1) for y in range(b + 1) for z in range(c + 1) if x + y + z != n])