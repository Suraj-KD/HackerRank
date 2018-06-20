'''
Task:
You have a test String S.
Your task is to write a regex which will match word starting with vowel (a,e,i,o, u, A, E, I , O or U). 
The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only. 
The matched word must start and end with a word boundary.
Input : Found any match?
Output : true
'''
import re
Regex_pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
print(str(bool(re.search(Regex_pattern, input()))).lower())
