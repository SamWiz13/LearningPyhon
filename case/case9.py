day = int(input("Day :"))
oy = int(input("Month :"))
day +=1
if  oy ==1 or oy ==3 or oy ==5 or oy ==7 or oy ==8 or oy ==10 or oy ==12:
    if day > 31:
        day =1
        oy +=1
if oy ==2:
    if day > 28:
        day =1
        oy +=1
if oy ==4 or oy ==6 or oy ==9 or oy ==11:
    if day >30:
        day =1
        oy +=1
if oy ==13:
    oy =1
if oy ==1:
    print(day," Yanvar")
if oy ==2:
    print(day, " Fevral")
if oy ==3:
    print(day," Mart")
if oy ==4:
    print(day, " Aprel")
if oy ==5:
    print(day," May")
if oy ==6:
    print(day," Iyun")
if oy ==7:
    print(day," Iyul")
if oy ==8:
    print(day," Avgust")
if oy ==9:
    print(day," Sentiyabr")
if oy ==10:
    print(day," Oktiyabr")
if oy ==11:
    print(day," Noyabr")
if oy ==12:
    print(day," Dekabr")
