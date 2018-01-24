import re
pat = r'^[0-9]+$'
n = input()
if bool(re.match(pat,n)):
    n = int(n)
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    print(sum)
else:
    print("Invalid input")
