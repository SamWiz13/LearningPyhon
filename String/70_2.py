a=input('a = ')
for i in range(len(a)):
    if a[i]==')':
        for j in range(i-1,-1,-1):
            if a[j]=='{' or a[j]=='[':
                print(i,"Shu qavs noto'g'ri qo'yilgan")
            if a[j]=='(':
                a=a[:j]+'0'+a[j+1:]
                a=a[:i]+'0'+a[i+1:]
                break
    if a[i]=='}':
        for j in range(i-1,-1,-1):
            if a[j]=='(' or a[j]=='[':
                print(i,"Shu qavs noto'g'ri qo'yilgan")
            if a[j]=='{':
                a=a[:j]+'0'+a[j+1:]
                a=a[:i]+'0'+a[i+1:]
                break
    if a[i]==']':
        for j in range(i-1,-1,-1):
            if a[j]=='{' or a[j]=='(':
                print(i,"Shu qavs noto'g'ri qo'yilgan")
            if a[j]=='[':
                a=a[:j]+'0'+a[j+1:]
                a=a[:i]+'0'+a[i+1:]
                break
index=100
for i in range(len(a)):
    if a[i]==')' or a[i]==']' or a[i]=='}':
        index=i
        break
    elif a[i]=='(' or a[i]=='[' or a[i]=='{':
        index=-1
        break
if index==100:
    print(0)
else:
    print(index)