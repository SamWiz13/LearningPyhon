import re
date =input("Date :")
if re.search(r"\d{1,2}[\./-]29[\./-](((19|20)(04|08|[2468][048]|[13579][26])))",date):
   print(date)
else:
    print("False")
