import re
urll =input("URL :")
if re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|"
              r"(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",urll):
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
