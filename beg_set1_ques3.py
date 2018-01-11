import re
pat  = r'^[a-zA-Z]$'
n = input()
if bool(re.match(pat,n)):
    if(n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u' or n == 'A' or n == 'E' or n == 'O' or n == 'U'):
        print("Vowel")
    else:
        print("consonant")
else:
    print("invalid input")
