import re
pat = r'^[0-9]+$'
n,k = input().split()
l = []
if bool(re.match(pat,n)) and bool(re.match(pat,k)):
    n = int(n)
    k = int(k)
    for i in range(1,n+1):
        l.append(i)
    print(" ".join(map(str,l)))
    sum = 0
    for i in range(1,k+1):
        sum = sum + i
    print(sum)

else:
    print("Invalid input")
