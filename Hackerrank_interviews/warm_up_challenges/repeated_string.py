import re

s = input()
n = int(input())

if s == 'a':
    print(n)
elif len(s) == 1:
    print(0)
elif n > len(s):
    fit, remainder = divmod(n, len(s))
    result = re.findall('a', s)
    if fit == 0:
        print(len(result) * fit)
    else:
        remainder_a = re.findall('a', s[:remainder])
        print((len(result) * fit + len(remainder_a)))
else:
    result = re.findall('a', s[:n])
    print(len(result))
