'''
In a galaxy far, far away, on a planet different from ours, each computer username uses the following format:

It must begin with either an underscore, _ (ASCII value 95), or a period, . (ASCII value 46).
The first character must be immediately followed by one or more digits in the range 0 through 9.
After some number of digits, there must be  or more English letters (uppercase and/or lowercase).
It may be terminated with an optional _ (ASCII value 95). Note that if it's not terminated with an underscore, then there should be no characters after the sequence of 0 or more English letters.
Given  strings, determine which ones are valid alien usernames. If a string is a valid alien username, print VALID on a new line; otherwise, print INVALID.

Input Format:

The first line contains a single integer, n, denoting the number of usernames. 
Each line  of the  subsequent lines contains a string denoting an alien username to validate.

Constraints:
1 <= n <= 100

Output Format:
Iterate through each of the  strings in order and determine whether or not each string is a valid alien username. If a username is a valid alien username, print VALID on a new line; otherwise, print INVALID.

Sample Input :
3
_0898989811abced_
_abce
_09090909abcD0

Sample Output:
VALID
INVALID
INVALID
'''
import re, sys
Regex_pattern = r'^[_.]\d+[a-zA-Z]*_?$'
for i in sys.stdin.readlines()[1:]:
    if re.match(Regex_pattern, i):
        print("VALID")
    else:
        print("INVALID")
