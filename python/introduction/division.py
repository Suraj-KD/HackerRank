'''
Read two integers and print two lines.
The first line should contain integer division, aa//bb.
The second line should contain float division, aa/bb.
# You don't need to perform any rounding or formatting operations.
# Input Format
# The first line contains the first integer, aa. The second line contains the second integer, bb.
# Output Format
# Print the two lines as described above.
'''
from __future__ import division
A = int(raw_input())
B = int(raw_input())
print A//B
print A/B
