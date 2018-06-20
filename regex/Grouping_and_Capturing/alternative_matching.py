'''
Task:
Given a test string, S, write a RegEx that matches S under the following conditions:
S must start with Mr., Mrs., Ms., Dr. or Er..
The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).
Input: Mr.DOSHI
Output: ture
'''
import re
Regex_pattern = r'^(?:Mr|Mr?s|Dr|Er)\.[a-zA-Z]+$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())
