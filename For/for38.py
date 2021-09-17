n = int(input("n :"))
s =0
for i in range(1,n+1):
    k = n-i+1
    for j in range(k,0,-1):
        s +=i**j
        print(i,j)
        break
print("Yig'indi: ",s)


