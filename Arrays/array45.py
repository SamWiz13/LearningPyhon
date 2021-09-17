from  random import  randint
n =int(input("N :"))
if  n >0:
      a =[randint(1,10) for i in range(n)]
      print(a)
      x =True
      for i in range(1,n):
          if x :
             mini =abs(a[i-1]-a[i])
             b=a[i-1]
             s =a[i]
             j =i
             x =False
          if  mini > abs(a[i-1] - a[i]):
              b =a[i-1]
              s =a[i]
              mini = abs(a[i - 1] - a[i])
              j =i
              print(b,end=" ")
              print(s,end=" ")
              print("Indeks :",j-1,i)