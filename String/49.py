s =input("str :")
s =s.split()
b =s[::-1]
print(b)
for i in range(len(b)):
    j =b[i][0]
    b[i] =b[i][1:]
    b[i] =str(b[i]).replace(j,".")
    b[i] =str(j) +str(b[i])
s=b[::-1]
print(*s)
