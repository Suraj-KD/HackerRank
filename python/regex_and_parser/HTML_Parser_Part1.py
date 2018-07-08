'''
Task:
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.

Format your results in the following way:

Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2
Here, the -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value. 
The > symbol acts as a separator of the attribute and the attribute value.

If an HTML tag has no attribute then simply print the name of the tag. 
If an attribute has no attribute value then simply print the name of the attribute value as None.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->).Comments can be multiline as well.

Input Format:
The first line contains integer N, the number of lines in a HTML code snippet.
The next N lines contain HTML code.

Constraints:
0 < N < 100

Output Format:
Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.

Use proper formatting as explained in the problem statement.

Sample Input:
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

Sample Output:
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
'''
import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,  tag, attrs):
        print("Start : " + tag)
        if attrs:
            for i in attrs:
                print("-> " + str(i[0]) + " > " + str(i[1]))
    def handle_endtag(self, tag):
        print("End   : " + tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty : " + tag)
        if attrs:
            for i in attrs:
                print("-> " + str(i[0]) + " > " + str(i[1]))
        
        
if __name__ == '__main__':
    parser = MyHTMLParser()
    text = sys.stdin.read()
    parser.feed(text)
