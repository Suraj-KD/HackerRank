import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
check = re.findall('(?<=['+c+'])(['+v+']{2,})(?=['+c+'])', input(), flags = re.I)
print('\n'.join(check or ['-1']))
