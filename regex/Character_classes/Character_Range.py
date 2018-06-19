import re
Regex_pattern = r'^[a-z]{1}[1-9]{1}[^a-z]{1}[^A-Z]{1}[A-Z]{1}'
print(str(bool(re.search(Regex_pattern, input()))).lower())
