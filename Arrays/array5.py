f=[0,1]
n =int(input("n :"))
for i in range(2,n+1):
    f.append(f[i-1]+f[i-2])
print(f)