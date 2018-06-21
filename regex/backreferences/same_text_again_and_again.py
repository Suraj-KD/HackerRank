'''
Task:
You have a test string S.
Your task is to write a regex that will match S with the following conditions:
S must be of length: 20
1st character: lowercase letter.
2nd character: word character.
3rd character: whitespace character.
4th character: non word character.
5th character: digit.
6th character: non digit.
7th character: uppercase letter.
8th character: letter (either lowercase or uppercase).
9th character: vowel (a, e, i , o , u, A, E, I, O or U).
10th character: non whitespace character.
1st character: should be same as 1st character.
2nd character: should be same as 2nd character.
3rd character: should be same as 3rd character.
4th character: should be same as 4th character.
5th character: should be same as 5th character.
6th character: should be same as 6th character.
7th character: should be same as 7th character.
8th character: should be same as 8th character.
9th character: should be same as 9th character.
10th character: should be same as 10th character.
Input : ab #1?AZa$ab #1?AZa$
Output : true
'''
import re
Regex_pattern = r'^([a-z]{1})(\w{1})(\s{1})(\W{1})(\d{1})(\D{1})([A-Z]{1})([a-zA-Z]{1})([aeiouAEIOU]{1})(\S{1})\1\2\3\4\5\6\7\8\9\10'
print(str(bool(re.search(Regex_Pattern, input()))).lower())
