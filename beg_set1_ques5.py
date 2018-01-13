import re
pat = r'^-?[0-9]+&'
n1 = input()
n2 = input()
n3 = input()
if bool(re.match(pat,n1) and re.match(pat,n2) and re.match(pat,n3)):
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    if (n1>n2 and n1>n3):
        print(n1)
    elif (n2>n3):
        print(n2)
    else:
        print(n3)
else:
    print("invalid input")
        
