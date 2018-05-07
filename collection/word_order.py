from collections import OrderedDict
import sys
ordereddict = OrderedDict()
seen = set()
INP = sys.stdin.readlines()
for word in INP[1:]:
    i = word.strip()
    if i in seen:
        ordereddict[i] += 1
    else:
        seen.add(i)
        ordereddict[i] = 1
print(len(ordereddict))
for key in ordereddict.keys():
    print(ordereddict[key], end=' ')
