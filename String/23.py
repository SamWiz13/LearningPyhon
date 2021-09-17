a =input('a = ')
s=0

for i in range(len(a)-1):
    if a[i] =='-':
        s -=int(a[i+1])
    if a[i] =='+':
        s +=int(a[i+1])
print(s)
