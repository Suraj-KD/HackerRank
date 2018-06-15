import re
pattern = r'^[+-]?[0-9]*\.[0-9]+$'
for i in range(int(input())):
    check = re.search(pattern, str(input()))
    print(bool(check))
