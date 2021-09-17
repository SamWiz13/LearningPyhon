n =int(input("n :"))
f =open("fiel3.txt","x")
for i in range(n):
    k =65
    for j in range(i+1):
        f.write(chr(k))
        k +=1
    f.write("\n")
f.close()
d =open('file3.txt','r')
print(d.read())
