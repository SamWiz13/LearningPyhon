def combi(n,k):
    if k==0 or k==n:
        return 1
    else: return combi(n-1, k-1) + combi(n-1, k)

n=int(input('n='))
k=int(input('k='))
print(combi(n,k))

