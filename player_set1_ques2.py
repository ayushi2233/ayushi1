import re
pat = r'^[+]?[0-9]+$'
n = input()
if bool(re.match(pat,n)):
    n = int(n)
    f = 1
    for i in range(1,n+1):
        f = f*i
        
        
    print(f)
else:
    print("invalid input")
        
        
