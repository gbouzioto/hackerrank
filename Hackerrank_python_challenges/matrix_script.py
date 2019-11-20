
import re


n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
string = ''
for i in range(m):
    for j in range(n):
        string += matrix[j][i]
# print(string)
pattern = r"\b[^a-zA-Z0-9]+\b"
re.compile(pattern)
new_string_list = re.split(pattern, string)
new_string = ''
for i in new_string_list:
    new_string += ' ' + i
new_string = new_string.lstrip(' ')
print(new_string)



# \b[^a-zA-Z0-9]+\b match the pattern between words
