s =input("satr :")
s =s.split()
x =True
for i in s:
    if x:
        mini =len(i)
        j =i
        x =False
    if mini > len(i):
        mini =len(i)
        j =i
print(j)
print(len(j))