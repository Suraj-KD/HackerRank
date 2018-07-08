'''
Task

You are given an HTML code snippet of N lines. 
Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:

#>>> Single-line Comment  
Comment
#>>> Data                 
My Data
#>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
#>>> Data
My Data
#>>> Single-line Comment:  
Note: Do not print data if data == '\n'.

Input Format

The first line contains integer N, the number of lines in the HTML code snippet.
The next N lines contains HTML code.

Constraints:
0 < N < 100

Output Format:
Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.

Format the answers as explained in the problem statement.

Sample Input:
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

Sample Output:
#>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
#>>> Data
 Welcome to HackerRank
#>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data" + "\n" + data)
    def handle_comment(self, comment):
        if comment.strip():
            lines = comment.split('\n')
            print(">>> ", "Multi" if len(lines) > 1 else "Single", "-line Comment", sep='')
            print(*lines, sep='\n')
  
  
if __name__ == '__main__':
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
