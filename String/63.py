s =input("str :")
k =int(input("k :"))
cipher= ""
for i in s:
    if s.isalpha():
      d = ord(i) + k
      if d > ord('z'):
         d  -= 26
      a = chr(d)
      cipher += a
print(cipher)
