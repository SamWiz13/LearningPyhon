s =input("str :")
s =s.split()
d =0
for i in s:
    if i.islower() and  i[0] ==i[-1]:
        i =i.upper()
        d +=1
        print(i,end=" ")
print()
print(d)

