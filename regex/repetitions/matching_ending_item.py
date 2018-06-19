'''
Task :
Write a RegEx to match a test string, S, under the following conditions:
S should consist of only lowercase and uppercase letters (no numbers or symbols).
S should end in s.
Input : Kites
Output : true
'''
import re
Regex_pattern = r'^[a-zA-Z]*s$'
print(str(bool(re.search(Regex_pattern, input()))).lower())
