import re
password = input("Password: ")
if re.findall(r"^.*(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",password):
    print("Awesome")
elif re.findall(r"^.*(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$",password):
    print("Not bad")
elif re.findall(r"^.*(?=.{8,})(?=.*[a-z]).*$",password):
    print("Bad")
