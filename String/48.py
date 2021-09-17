s =input("str :")
s =s.split()
for i in range(len(s)):
    j =s[i][0]
    s[i] =s[i][1:]
    s[i] =str(s[i]).replace(j,".")
    s[i] =str(j) +str(s[i])
print(*s)
