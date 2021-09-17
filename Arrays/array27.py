n=int(input('n = '))
a=[int(input('a = ')) for i in range(n)]
print(a)

for i in range(len(a)-1):
    if a[i]*a[i+1]>=0:
        print(i+1,end=' Tugadi')
        break
else:
    print("0")