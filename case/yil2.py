yil =int(input("Year :"))
oy = int(input("Month :"))
day = int(input("Day :"))
day +=1
if  oy ==1 or oy ==3 or oy ==5 or oy ==7 or oy ==8 or oy ==10:
    if day > 31:
        day =1
        oy +=1
if oy ==12:
        day =1
        oy +=1
if oy ==2:
    if  day >28 and (yil % 4 ==0  and yil % 100 !=0 or yil % 400==0):
        day =29
    else:
        day =1
        oy +=1
if oy ==4 or oy ==6 or oy ==9 or oy ==11:
    if day >30:
        day =1
        oy +=1
if oy ==13:
    day =1
    oy =1
    yil +=1
if oy ==1:
    print(yil,day," Yanvar")
if oy ==2:
    print(yil,day, " Fevral")
if oy ==3:
    print(yil,day," Mart")
if oy ==4:
    print(yil,day, " Aprel")
if oy ==5:
    print(yil,day," May")
if oy ==6:
    print(yil,day," Iyun")
if oy ==7:
    print(yil,day," Iyul")
if oy ==8:
    print(yil,day," Avgust")
if oy ==9:
    print(yil,day," Sentiyabr")
if oy ==10:
    print(yil,day," Oktiyabr")
if oy ==11:
    print(yil,day," Noyabr")
if oy ==12:
    print(yil,day," Dekabr")