'''
NOTE:THIS CODE WORKS IN PYTHON-2.7
Input Format:
A single line of input consisting of the string .
Output Format:
A single line of output consisting of the modified string.
Constraints:
All the characters of S denote integers between 0 and 9.
1 <= |S| <= 10^4
Sample Input:
1222311
Sample Output:
(1, 1) (3, 2) (1, 3) (2, 1)
Explanation:
First, the character 1 occurs only once. It is replaced by (1, 1).
Then the character 2 occurs three times, and it is replaced by
(3, 2) and so on.
Also, note the single space within each compression and between the compressions.
'''
from itertools import groupby
S = raw_input()
for k, g in groupby(S):
    print(tuple((len(list(g)), int(k)))),

'''
Note: THIS CODE WORKSIN PYTHON-3
from itertools import groupby
S = input()
for k, g in groupby(S):
    print(tuple((len(list(g)), int(k))), end=' ')
'''

