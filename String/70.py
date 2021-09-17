s = input("s = ")
k = 1
if s.count("(") != s.count(")") or s.count("[") != s.count("]") or s.count("{") != s.count("}"):
   k = 0
print("-1")
a = ["(", "[", "{"]; b = [")", "]", "}"]
if k:
    m = sum(s.count(j) for j in a)
    q = 0
    bosh = -1; oxir = len(s)
    for i in s:
        if i in a:
           if i == a[0]:
                 w = 0
           elif i == a[1]:
                w = 1
           else:
                w = 2
                q += 1
                bosh = s[bosh + 1:].find(a[w]) + bosh + 1
                oxir = s[:oxir].rfind(b[w])
        if bosh > oxir:
            print(bosh, len(s) - 1 - s[::-1].rfind(b[w]))
            k = 0
            break
        if q == m:
                break
if k:
    print(0)