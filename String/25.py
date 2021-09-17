s =int(input("satr :"))
S =''
while True:
    d =s %2
    S +=str(d)
    s //=2
    if  s ==0:
        break
S =S[::-1]
print(S)