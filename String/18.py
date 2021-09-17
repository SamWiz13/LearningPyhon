s =input("Satr :")
a =''
for i in s:
    if i.isupper():
        a +=i.lower()
    if i.islower():
        a +=i.upper()
print(a)