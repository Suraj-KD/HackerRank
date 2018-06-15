'''
Task:
You are given a string S.
Your task is to print all possible combinations, up to size k,
of the string in lexicographic sorted order.
Input:
A single line containing the string S and integer value k separated by a space.
Output:
Print the different combinations of string S on separate lines.
Sample Input:
HACK 2
Sample Output:
A
C
H
K
AC
AH
AK
CH
CK
HK
'''
from itertools import combinations
INPUT = raw_input().split()
for i in range(1, int(INPUT[1]) + 1):
    l = sorted(list(combinations(sorted(INPUT[0]), i)))
    print '\n'.join(''.join(elems) for elems in l)
