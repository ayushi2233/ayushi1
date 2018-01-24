import re
pat = r'^[0-9]+$'
n = input()
if bool(re.match(pat,n)):
    n = int(n)
    for i in range(0,n):
        print("Hello")
else:
    print("Invalid input")
