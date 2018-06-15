import sys
INP = [lines.strip() for lines in sys.stdin.readlines()]
position = [i for i in range(len(INP[1].strip().split())) if INP[1].strip().split()[i] == 'MARKS'][0]
print(format(sum([int(data.strip().split()[position]) for data in INP[2:]])/float(len([int(data.strip().split()[position]) for data in INP[2:]])), '.2f'))


# 2nd way  to solve using collections.namedtuple
import sys
from collections import namedtuple
INP = [lines.strip().split() for lines in sys.stdin.readlines()]
Row = namedtuple('row', INP[1])
print(format(sum([int(Row(*line).MARKS) for line in INP[2:]])/float(len([int(Row(*line).MARKS) for line in INP[2:]])), '.2f'))
