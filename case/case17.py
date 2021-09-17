y = int(input("Masala sonini kiriting:"))
on = y // 10
bir = y % 10
if  on == 1:
    print("O'n",end=" ")
if  on == 2:
    print("Yigirma",end=" ")
if  on == 3:
    print("O'ttiz",end=" ")
if  on == 4:
    print("Qiriq",end=" ")
if  on == 5:
    print("Ellik",end=" ")
if  on == 6:
    print("Oltmish",end=" ")
if  on == 7:
    print("Yetmish",end=" ")
if  on == 8:
    print("Sakson",end=" ")
if  on == 9:
    print("To'qson",end=" ")
if  bir == 1:
    print("bitta masala")
if  bir == 2:
    print("ikkita masala")
if  bir == 3:
    print("uchta masala")
if  bir == 4:
    print("to'rt ta masala")
if  bir == 5:
    print("besh ta masala")
if  bir == 6:
    print("olti ta masala")
if  bir == 7:
    print("yetti ta masala")
if  bir == 8:
    print("sakkiz ta masala")
if  bir == 9:
    print("to'qqiz ta masala")
if y == 0:
    print("Masala yoq")