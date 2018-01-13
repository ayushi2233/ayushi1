import re
pat = r'^[a-zA-Z]+$'
n = input()
rev = []
if bool(re.match(pat,n)):
    rev = n[::-1]
    print(rev)
else:
    print("invalid input")
