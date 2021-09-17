import  re
nomber =input("Nomer :")

if re.match("\+998[0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2}$",nomber):
        print(nomber)
else:
    print("False")


