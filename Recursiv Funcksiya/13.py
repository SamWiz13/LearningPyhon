n =input("n :")
def Polindrom(n):
    if n ==n[::-1]:
        return True
    else:
        return False
print(Polindrom(n))