a = int(input("a :"))
b = int(input("b :"))
n = int(input("n :"))
x = abs(a-b)/n
mini = min(a,b)
for i in range(n+1):
    print(round(mini),1,end=" ")
    mini = x