import re
pat = r'^[0-9]{4}$'
n = input()
if bool(re.match(pat,n)):
    n = int(n)
    if(n%4 == 0 and n%100!=0):
        print("yes")
    elif(n%400 == 0):
        print("yes")
    else:
        print("no")
else:
    print("invalid input")
