def DigitSum(k):
    if k <10:
       return k
    return DigitSum(k //10) +k %10
k =int(input("K :"))
print(DigitSum(k))
