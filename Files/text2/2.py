n=int(input('n='))
f=open('file2.txt','w')
for i in range(n):
    k=97
    for j in range(i+1):
        f.write(chr(k))
        k+=1
    f.write('\n')
f.close()
d=open('file2.txt','r')
print(d.read())



