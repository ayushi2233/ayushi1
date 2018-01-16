import re
pat = r'^[+]?[0-9]+$'
n = input()
if bool(re.match(pat,n)):
    rev = []
    rev = n[::-1]
    print(rev)
else:
    print("invalid input")
        
    
