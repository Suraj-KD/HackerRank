import sys


l = [int(i) for i in sys.stdin.readlines()[1].strip().split()]
print(all(v >= 0 for v in l) and any(str(x) == str(x)[::-1] for x in l))
