'''
You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.

Input Format:
The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format:
Output a single line, the integer score of the given XML document.

Sample Input:
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output:
5

Explanation::
The feed and subtitle tag have one attribute each - lang. 
The title and updated tags have no attributes. 
The link tag has three attributes - rel, type and href. 

So, the total score is 1 + 1 + 3 = 5. 

There may be any level of nesting in the XML document.
'''
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    count = 0
    if node.attrib:
        count += len(node.attrib)
    for child in node.findall('.//'):
        count += len(child.attrib)
    return count


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print get_attr_number(root)
