c =input("c :")
s1 =input("Satr :")
s2 =input("Satr :")
if s1.count(c):
    s1=s1.replace(c,s2+c)
    print(s1)
else:
    print("Satrda bu belgi yoq.")