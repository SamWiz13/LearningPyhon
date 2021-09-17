n =int(input("n :"))
fayl1 =input("Fayl beginner :")
fayl2 =input("Fayl end :")
with open(fayl1 +".txt")as f:
    a =f.read()
a =a.split("\n")
print(a)
i =0
while i < len(a) -1:
    if len(a[i]) > n:
        while len(a[i]) > n:
            m =a[i].split()[-1] +" "
            a[i] =a[i][:a[i].rfind(" ")]


