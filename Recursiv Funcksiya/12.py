s =int(input("s :"))
dcount =0
def DigitCount(s):
    global dcount
    if s <10:
        return s
    s //=10
    dcount +=1
    return dcount
print(DigitCount(s))