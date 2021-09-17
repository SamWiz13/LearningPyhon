n = int(input('n :'))
s = int(input('s :'))
while True:
    if 10**n >s:
        print('Javob :',s%10)
        break
    s=s // 10