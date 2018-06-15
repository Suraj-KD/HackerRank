import re
regex_pattern = r'([a-zA-Z0-9])\1+'
m = re.search(regex_pattern, input())
print(m.group(1) if m else -1)
