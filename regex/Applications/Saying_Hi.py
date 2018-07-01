'''
Given a sentence, s, write a RegEx to match the following criteria:

The first character must be the letter H or h.
The second character must be the letter I or i.
The third character must be a single space (i.e.: \s).
The fourth character must not be the letter D or d.
Given n lines of sentences as input, print each sentence matching your RegEx on a new line.

Input Format:
The first line contains an integer, n, denoting the number of lines of sentences.
Each of the n subsequent lines contains some sentence s you must match.

Constraints:
1 <= n <= 10
Each sentence, s, contains 1 to 10 words.
Each word/token in a sentence is comprised only of upper and lowercase English letters.

Output Format:
Find each sentence, s, satisfying the RegEx criteria mentioned above, and print it on a new line.

Sample Input:
5
Hi Alex how are you doing
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha by saying Hi Martha

Sample Output:
Hi Alex how are you doing
'''
import re

if __name__ == "__main__":
    Regex_pattern = r'^[Hh][Ii]\s[^Dd].*'

    n = int(input())
    for nr in range(n):
        line = input()
        find = re.search(Regex_pattern, line)

        if find:
            print(line)
