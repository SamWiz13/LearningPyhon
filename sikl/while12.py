n = int(input("n ="))
k =0
s =0
while s <n:
       k += 1
       s += k
       if   s >n:
           s -=1
           k -=1
print(k)
print(s)