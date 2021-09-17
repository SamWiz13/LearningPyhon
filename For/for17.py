n = int(input("Darajani kiriting = "))
a = int(input("Sonni kiriting ="))
s =1/a; y =0
for i in range(1,n +1):
    s *=a
    y +=s
    print(i, s)
print("Yig'indi:",y)