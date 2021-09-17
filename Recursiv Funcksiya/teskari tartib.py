def teskari(k):
    if len(k) ==1:
        return k
    return k[-1] +teskari(k[:len(k)-1])
print(teskari(input("k :")))
