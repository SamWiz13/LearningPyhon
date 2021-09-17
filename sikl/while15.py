s = float(input("s ="))
p = float(input("f ="))
k =0
t = 2*s

while s <=t:
    s +=s*p / 100
    k +=1
print(k)