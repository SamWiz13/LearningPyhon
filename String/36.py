s1 =input("Str1 :")
s2 =input("Str2 :")
if s1.count(s2):
   s3=s1.replace(s2,"",1)
   print(s3)
else:
    print(s1)