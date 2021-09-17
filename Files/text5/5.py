s =input("s :")
with open("..\\filee","r") as file:
    a =file.read()
with open("..\\filee","a") as fileee:
    a =fileee.write(s)
print(a)
