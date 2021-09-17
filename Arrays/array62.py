from  random import  randint
n =int(input("N :"))
a =[randint(1,10) for i in range(n)]
b =[randint(-10,-1) for i in range(n)]
print(a)
s =0
for i in range(len(b)):
    s +=1
print(b,"Index soni :",s)
for i in range(n):
    c =a[:] +b[:]
    s +=1
print(c,"index soni :",s)