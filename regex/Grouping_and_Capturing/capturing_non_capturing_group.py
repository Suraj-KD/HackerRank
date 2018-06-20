'''
Task:
You have a test String S. 
Your task is to write a regex which will match S with the following condition:
S should have 3 or more consecutive repetitions of ok.
Input: okokok! cya
Output: true
'''
import re
Regex_pattern = r'(ok){3,}'
print(str(bool(re.search(Regex_Pattern, input()))).lower())
