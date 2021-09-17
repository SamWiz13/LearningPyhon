n = int(input("n ="))
i = 1; a0 =1
while i <=n:
    ai = i*a0+1/i
    a0 = ai
    i +=1
print("Yig'indi: ",ai)