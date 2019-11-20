n = int(input())
s = input()

down = 0
up = 0
valleys = 0
landscape = ''
for i in range(n):
    if s[i] == 'U':
        up += 1
    else:
        down += 1
    landscape += s[i]
    if up == down:
        if landscape.startswith('D'):
            valleys += 1
        up = 0
        down = 0
        landscape = ''
print(valleys)
