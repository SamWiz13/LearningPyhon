import string
s =input("satr :")
b =0
for i in s:
    if i in string.punctuation:
        b +=1
        print(i,end=" ")
print()
print(b)