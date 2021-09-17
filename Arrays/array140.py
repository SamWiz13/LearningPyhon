from  random import  randint
n =int(input("N :"))
x =[randint(-10,10) for i in range(n)]
y =[randint(-10,10) for i in range(n)]
print("X :",x)
print("Y :",y)

for i in range(n-1):
    for j in range(i+1,n):
        if x[i] +y[i] < x[j] + y[j] or x[i] + y[i] == x[j] + y[j] and x[i] < x[j]:
               x[i], x[j], y[i], y[j] =x[j], x[i],y[j],y[i]

print("X sort :",x)
print("Y sort :",y)