a = int(input("a ="))
uzunlik =input("Uzunlik turini kiriting:")

if  uzunlik =='km':
    print(a * 1000," metr")
elif uzunlik =='dm':
    print(a / 10, "metr ")
elif uzunlik =='sm':
    print(a / 100," metr")
elif uzunlik =='m':
    print(a," m")
elif  uzunlik =='mm':
    print(a / 10000, " metr")