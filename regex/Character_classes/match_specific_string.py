import re
Regex_pattern = r'^[123]{1}[120]{1}[xs0]{1}[30Aa]{1}[xsu]{1}[.,]{1}$'
print(str(bool(re.search(Regex_pattern, input())).lower())
