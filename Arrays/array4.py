n =int(input("n :"))
b =[int(input("b :"))]
q =float(input("q :"))

for i in range(1,n):
    b.append(b[i-1]*q)
print(b)