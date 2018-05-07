from collections import OrderedDict
import sys, re
orderdict = OrderedDict()
seen = set()
INP = sys.stdin.readlines()
for line in INP[1:]:
    item = re.split(r'\s{1}', line.strip())
    if ' '.join(item[:-1]) in seen:
        orderdict[' '.join(item[:-1])] += int(item[-1])
    else:
        seen.add(' '.join(item[:-1]))
        orderdict[' '.join(item[:-1])] = int(item[-1])
for  key in orderdict.keys():
    print(key, orderdict[key], sep=' ')
