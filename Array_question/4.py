from  random import  randint
n =int(input("N :"))
a =[randint(1,100) for i in range(n)]
print(a)
x =True
for i in range(n):
      if x:
            mini =a[i]
            j =i
            x =False
      if mini >a[i]:
            mini =a[i]
            j =i
print("Element :",a[j])
print("Index :",j)

