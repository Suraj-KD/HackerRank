'''
We define a word as a non-empty maximum sequence of characters that can contain only lowercase letters, uppercase letters, digits and underscores '_' (ASCII value 95). Maximum sequence means that the word has to be immediately preceeded by a character not allowed to occur in a word or by the left boundary of the sentence, and it has to be immediately followed by a character not allowed to occur in a word or by the right boundary of the sentence.
Given N sentences and T words, for each of these words, find the number of its occurences in all the N sentences.

Input Format:
In the first line there is a single integer N. Each of the next N lines contains a single sentence. After that, in the next line, there is a single integer T denoting the number of words. In the i-th of the next T lines, there is a single word denoting the i-th word for which, you have to find the number of its occurences in the sentences.

Constraints:
1 <= N <= 100
1 <= T <= 10 

Output format:
For every word, print the number of occurrences of the word in all the N sentences listed.

Sample Input:
1
foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.
1
foo

Sample Output:
6
'''
import re
list_of_lines, list_of_queries = list(), list()
# Number of lines
num_of_line = int(input())
# Input Lines stored in a  list
for _ in range(num_of_line):
    list_of_lines.append(input())
# Number to queries
num_of_query = int(input())
# Input Queries stored in list
for _ in range(num_of_query):
    list_of_queries.append(input())
for query in list_of_queries:
    count = 0
    # Regex to find the query in required format
    Regex_pattern_query = re.compile(r'(?<!\w)' + query + '(?!\w)')
    for line in list_of_lines:
        # Regex to split the line into list of words
        Regex_pattern_line = re.compile(r'\W?\w+\W?')
        word_list = re.findall(Regex_pattern_line, line)
        for word in word_list:
            if re.search(Regex_pattern_query, word):
                count += 1
    print(count)
