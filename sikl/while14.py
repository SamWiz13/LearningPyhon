a = float(input("a ="))
k =0
s =0
while s <a:
       k += 1
       s += 1/k
       if   s >a:
        s -=1/k
        k -=1
print(k)
print(s)