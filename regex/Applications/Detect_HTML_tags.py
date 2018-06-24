'''
Task:
Given N lines of HTML, find the tag names (ignore any attributes) and print them as a single line of lexicographically ordered semicolon-separated values (e.g.:tag1;tag2;tag3).

Input Format:
The first line contains an integer, N, the number of HTML fragments. 
Each of the N subsequent lines contains a fragment of an HTML document.

Constraints:
1 <= N <= 100
Each fragment contains < 10000 ASCII characters.
The fragments are chosen from Wikipedia, so analyzing and observing their markup structure may help.
Leading and trailing spaces/indentation have been trimmed from the HTML fragments.
Output Format:
Print a single line containing all of the unique tag names found in the input. Your output tags should be semicolon-separated and ordered lexicographically (i.e.: alphabetically). Do not print the same tag name more than once.

Sample Input:
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

Sample Output:
a;div;p
'''
import re, sys
Regex_pattern = r'<\s*(\w+)'
tag_list = list()
for i in sys.stdin.readlines()[1:]:
    splitted_line = re.split('(<\s*(\w+))', i)
    for sub in splitted_line:
        match = re.search(Regex_pattern, sub)
        if match:
            tag_list.append(str(match.group(1)))
tag_list = sorted(set(tag_list))
print(';'.join(tag_list))
