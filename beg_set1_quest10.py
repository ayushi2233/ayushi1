import re
pat = r'^[-]?[0-9]+$'
n = input()
if bool(re.match(pat,n)):
    n = str(n)
    l = len(n)
    print(l)
    
else:
    print("invalid input")
        
