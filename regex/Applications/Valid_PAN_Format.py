'''
Task:
The equivalent of SSN in India is a PAN number, which is unique to each of its citizens. In any of the country's official documents, the PAN number is listed as follows

<char><char><char><char><char><digit><digit><digit><digit><char>
Your task is to figure out if the PAN number is valid or not. A valid PAN number will have all its letters in uppercase and digits in the same order as listed above.

Input Format:
First line contains .  lines follow, each having a PAN number.

Constraints:
1 <= N <= 10
Each char is an uppercase letter, i.e., .
Each digit lies between 0 and 9, i.e., .
The length of the PAN number is always 10, i.e.,
Every character in PAN is either char or digit satisfying the above constraints.

Output Format:
For every PAN number listed, print YES if it is valid and NO if it isn't.

Sample Input:
3
ABCDS1234Y
ABAB12345Y
avCDS1234Y

Sample Output:
YES
NO
NO
'''
import re, sys
Regex_pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')
for i in sys.stdin.readlines()[1:]:
    if re.match(Regex_pattern, i):
        print("YES")
    else:
        print("NO")
