import re
pat1 = r'^[+]?[0-9]+$'
pat2 = r'^[-]?[0-9]+$'
n = input()
if bool(re.match(pat1,n)):
    n = int(n)
    f = 1
    for i in range(1,n+1):
        f = f*i
    print(f)
elif bool(re.match(pat2,n)):
    print(0)
        
else:
    print("invalid input")
        
        
