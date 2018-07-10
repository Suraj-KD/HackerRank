'''
Neo has a complex matrix script. The matrix script is a N X M grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

Matrix Script
T  s  i
h  %  x
i     #
s  M  
$  a  
#  t  %
i  r  !

Matrix Decoded:
This$#is% Matrix# %!

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format:
The first line contains space-separated integers N (rows) and M (columns) respectively. 
The next N lines contain the row elements of the matrix script.

Constraints:
0 < N,M < 100

Note: A 0 score will be awarded for using 'if' conditions in your code.

Output Format:
Print the decoded matrix script.

Sample Input:
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

Sample Output:
This is Matrix#  %!

Explanation:
The decoded script is:

This$#is% Matrix#  %!
Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.

So, the final decoded script is:

This is Matrix#  %!
'''
import re


if __name__ == '__main__':
    matrix = []
    N,M = map(int, input().split())
    for _ in range(N):
        matrix.append(list(input()))
        print(re.sub(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])',' ',"".join("".join(decode) for decode in zip(*matrix))))
