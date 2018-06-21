'''
Task:
You have a test string S.
Write a regex that can match all occurrences of o followed immediately by oo in S.
Input: gooooo!
Output: Number of matches : 3
'''
import re
Regex_pattern = r'o(?=oo)'
Test_String = input()
match = re.findall(Regex_pattern, Test_String)
print("Number of matches :", len(match))
