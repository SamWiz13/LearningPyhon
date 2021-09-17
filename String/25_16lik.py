s = input("s = ")
S = ""
while s != "0":
    if int(s) % 16 < 10:
        S = str(int(s) % 16) + S
    else:
        S = str(chr(55 + int(s) % 16)) + S
    s = str(int(s) // 16)
print(S)