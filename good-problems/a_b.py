a = int(input("a :"))
b = int(input("b :"))
s=0
for i in range(0,b):
    s+=(a+i)**(b-i)
    print(s,end=" ")
print()
print(s)
