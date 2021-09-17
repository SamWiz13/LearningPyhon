n=int(input('n = '))
a=[int(input('a = ')) for i in range(n)]
print(a)

for i in range(len(a)-1):
    if a[i] <a[i+1]:
        print(a[i],end=" ")
else:
    print("0")
