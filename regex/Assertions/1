'''
Task:
You have a test String S.
Write a regex which can match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).
Input: 1o1s
Output: Number of matches : 3
'''
import re
Regex_pattern = r'(?<![aeiouAEIOU]).'
Test_String = input()
match = re.findall(Regex_pattern, Test_String)
print("Number of matches :", len(match))

