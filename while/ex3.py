n = int(input("n ="))
i =1; s =0
while i <n:
    if n % i ==0:
        s +=i
    i +=1
if  s ==n:
    print("Mukkamal son")
else:
    print("Mukkamal emas")
