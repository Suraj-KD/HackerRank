'''
Task
You have a test string S. 
Your task is to write a regex that will match S using the following conditions:
S must be of length equal to 45.
The first  characters should consist of letters(both lowercase and uppercase), or of even digits.
The last  characters should consist of odd digits or whitespace characters.

Input : 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
Output : true
'''
import re
Regex_pattern = r'^[02468a-zA-Z]{40}[13579\s]{5}$'
print(str(bool(re.search(Regex_pattern, input()))).lower())
