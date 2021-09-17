f =open("D:\\Python online kurs\\Files\\text2\\file2.txt",'r')
k =0
j =0
for i in f:
    k +=1
    j +=len(i)
print(k)
print(j)
f.close()