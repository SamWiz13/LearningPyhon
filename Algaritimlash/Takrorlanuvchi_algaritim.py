a =int(input("a :"))
s =0
for i in range(1,4):
    s1 =0
    for j in range(1,4):
        s1 +=(a*i +j)
    s +=s1
print(s)