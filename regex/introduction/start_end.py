import re
Regex_Pattern = r"^\d\w{4}\.$"
print(str(bool(re.search(Regex_Pattern, input()))).lower())
