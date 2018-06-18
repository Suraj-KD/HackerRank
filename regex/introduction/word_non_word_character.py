import re
Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"
print(str(bool(re.search(Regex_Pattern, input()))).lower())
