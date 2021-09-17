k =int(input("k :"))
fayl1 =input("Fayl beginner :")
fayl2 =input("Fayl end :")
with open(fayl1 +".txt")as f:
    a =f.read()
a =a.split("\n")
i =0
while i < len(a):
    a[i] =a[i].split("\n")
    i +=1



with open(fayl2 +".txt")as fiyl:
    print(fiyl.read())

