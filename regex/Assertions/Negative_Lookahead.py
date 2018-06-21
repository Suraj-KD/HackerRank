'''
Task:
You have a test String S.
Write a regex which can match all characters which are not immediately followed by that same character.
Example:
If S = goooo, then regex should match goooo. Because the first g is not follwed by g and the last o is not followed by o.
Input: gooooo
Output: Number of matches : 2
'''
import re
Regex_pattern = r'(.)(?!\1)'
Test_String = input()
match = re.findall(Regex_pattern, Test_String)
print("Number of matches :", len(match))

