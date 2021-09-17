import  re
urll =input("URL :")
if re.findall(r'(\w+)://([\w\-\.]+)/(\w+).(\w+)',urll):
   print(urll)
else:
    print(False)


"""
URl
http://uw6ojivprppac546.onion
http://jbjuxuvhhmggqdrq.onion
https://www.youtube.com
https://pastebin.com/u/zurael_sTz
"""