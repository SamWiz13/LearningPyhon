from  random import  randint
a=[randint(1,10) for i in range(20)]
print(a, end="\n")
k=0
while k<len(a):
    son=a[k]
    #print("Yangi :",a)
    for i in range(a.count(son)):
        a.remove(son)
       # print(a)
    a.insert(k,son)
    k+=1
print(a)