'''
Task :
You have a test string S. 
Your task is to write a regex that will match S using the following conditions:
S should begin with 1 or more digits.
After that, S should have 1 or more uppercase letters.
S should end with 1 or more lowercase letters.
Input : 1Qa
Output : true
'''
import re
Regex_pattern = r'^\d+[A-Z]+[a-z]+$'
print(str(bool(re.search(Regex_pattern, input()))).lower())
