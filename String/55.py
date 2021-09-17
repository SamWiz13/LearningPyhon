s =input("satr :")
s =s.split()
x =True
for i in s:
    if x:
        maxi =len(i)
        j =i
        x =False
    if maxi <len(i):
        maxi =len(i)
        j =i
print(j)