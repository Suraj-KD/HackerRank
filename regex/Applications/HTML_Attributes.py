'''
Charlie's second assignment was given by the Professor as soon as he submitted the first one. Professor asked Charlie to create a list of all the attributes of every tag found in HTML pages.

<p>This is a paragraph</p> 
The above HTML string has p as its tag but no attributes.

<a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a>
This string has a as a tag and href as an attribute.

Input Format:
The first line contains N, the number of lines in the HTML fragment. This is followed by lines from a valid HTML document or fragment.

Constraints :
Number of characters in the test fragments <= 10000 characters. Characters will be restricted to ASCII. Fragments for the tests will be picked up from Wikipedia. 
Attributes are all lowercase alphabets.

Output Format :
Each tag must be separated by a newline arranged in lexicographic order 
Each attribute noted for a given tag must be arranged next to a tag in lexicographic order.

The output will be of the format

tag-1:attribute-1,attribute-2,attribute-3....
tag-2:attribute-1,attribute-2,attribute-3....
tag-3:attribute-1,attribute-2,attribute-3....
...
tag-n:attribute-1,attribute-2,attribute-3....
Where tag-1 is lexicographically smaller than tag-2 and attribute-1 is lexicographically smaller than attribute-2

Sample Input:1 :
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

Sample Output:1 :
a:href
div:class
p:
'''
import re, sys


if  __name__ == '__main__':
    num_of_lines = int(input())
    db = dict()
    Regex_pattern_tag = re.compile(r'.*<(\w+)')
    Regex_pattern_attribute = re.compile(r'(\w+)=')
    for line in range(num_of_lines):
        line = input()
        splitted_line = re.split(r' |>', line)
        for i in splitted_line:
            if (Regex_pattern_tag.match(i)):
                m = Regex_pattern_tag.match(i)
                if m.group(1) not in db:
                    db[m.group(1)] = []
            elif (Regex_pattern_attribute.match(i)):
                n = Regex_pattern_attribute.match(i)
                if n.group(1) not in db[m.group(1)]:
                    db[m.group(1)].append(n.group(1))
    for x in sorted(db.keys()):
        out = x + ":"
        db[x].sort()
        print(out+','.join(db[x]))
