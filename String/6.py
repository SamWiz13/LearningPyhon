a =input('a :')
b =ord(a)
if b >=ord("0") and  b <=ord("9"):
    print("Digit")
elif b >=ord("a") and b <=ord("z") or b >=ord("A") and b <=ord("Z"):
    print("Lotin")
else:
    print(0)

