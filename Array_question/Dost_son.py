n =int(input("N :"))
for i in range(1,n):
    s=0
    for j in range(1,i//2 +1):
        if i %j ==0:
            s +=j
    if s >i:
        k =0
        for j in range(1,s//2 +1):
            if s %j ==0:
                k +=j
        if k ==i and k !=s:
            print(k,s)
