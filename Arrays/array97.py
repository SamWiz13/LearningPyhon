from  random import  randint
n =int(input("N :"))
a=[randint(1,10) for i in range(n)]
print(a, end="\n")
k =0
while k <len(a):
      son=a[k]
      for i in range(a.count(son)):
             a.remove(son)
      a.insert(k,son)
      k+=1
print(a)