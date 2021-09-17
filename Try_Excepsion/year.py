import re
year =input("a :")
print("01-01-2000 OR 1-1-2000")

if re.match(r"(\d{1,2})-(\d{1,2})-(\d{4})$",year):
    print(year)
else:
    print("False")