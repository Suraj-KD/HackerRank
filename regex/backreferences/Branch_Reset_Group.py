'''
Task:
You have a test string S.
Your task is to write a regex which will match S, with following condition(s):
S consists of 8 digits.
S must have "---", "-", "." or ":" separator such that string S gets divided in 4 parts, with each part having exactly two digits.
S string must have exactly one kind of separator.
Separators must have integers on both sides.
Input : 12-34-56-78
Output : true
'''
import re
Regex_pattern = r'^\d{2}((---)|(-)|(,)|(.)|(:))\d{2}\1\d{2}\1\d{2}$'
print(str(bool(re.search(Regex_pattern, input()))).lower())

#Regex for Perl code
#Regex_pattern = r'^\d{2}(?|(---)|(-)|(,)|(.)|(:))\d{2}\1\d{2}\1\d{2}$'
