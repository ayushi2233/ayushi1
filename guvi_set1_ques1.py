import re
pat = r'-?[0-9]+'
a = input()
if bool(re.match(pat,a)):
    a = int(a)
    if(a > 0):
        print("Positive")
    if(a < 0):
        print("Negative")
    if(a == 0):
        print("Zero")
else:
    print("invalid input")
