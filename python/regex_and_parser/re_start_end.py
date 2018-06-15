import re

S = input()
k = input()
p = re.compile(r'(?=('+k+'))', re.VERBOSE)
if p.search(S):
    for m in p.finditer(S):
        print((m.start(1), m.end(1)-1))
else:
    print((-1, -1))
