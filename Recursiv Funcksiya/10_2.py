def DigitSum(k):
    if len(k) ==1:
       return int(k)
    return DigitSum(k[:len(k)-1]) +int(k[-1])
print(DigitSum(input("k :")))