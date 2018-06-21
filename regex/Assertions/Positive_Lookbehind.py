'''
Task:
You have a test String S.
Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.
Input: 123Go!
Output: Number of matches : 1
'''
import re
Regex_pattern = r'(?<=[13579])\d'
Test_String = input()
match = re.findall(Regex_pattern, Test_String)
print("Number of matches :", len(match))

