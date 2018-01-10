import re
pat = r'[0-9]+'
n = input()
if bool(re.match(pat,n)):
    n = int(n)
    if(n%2 == 0):
        print("Even")
    else:
        print("Odd")
else:
    print("invalid input")
