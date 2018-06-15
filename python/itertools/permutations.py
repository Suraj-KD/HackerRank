'''
Task:
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
Input Format :
A single line containing the space separated string S and the integer value k.
Output:
Print the permutations of the string S on separate lines.
Sample Input:
HACK 2
Sample Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''
from itertools import permutations
S, k = raw_input().split(' ')
for p in sorted([''.join(p) for p in list(permutations(S, int(k)))]):
    print p
