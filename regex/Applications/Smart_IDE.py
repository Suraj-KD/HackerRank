'''
Jack wants to build an IDE on his own. Help him build a feature which identifies the comments, in the source code of computer programs. Assume, that the programs are written either in C, C++ or Java. The commenting conventions are displayed here, for your convenience. At this point of time you only need to handle simple and common kinds of comments. You don't need to handle nested comments, or multi-line comments inside single comments or single-comments inside multi-line comments.

Your task is to write a program, which accepts as input, a C or C++ or Java program and outputs only the comments from those programs. Your program will be tested on source codes of not more than 200 lines.

Comments in C, C++ and Java programs

Single Line Comments:
// this is a single line comment
x = 1; // a single line comment after code

Multi Line Comments:
/* This is one way of writing comments */ 
/* This is a multiline 
   comment. These can often
   be useful*/

Input Format 
Each test case will be the source code of a program written in C or C++ or Java.

Output Format 
From the program given to you, remove everything other than the comments.
'''
import re, sys
Regex_pattern = r'/\*.*?\*/|//.*?$'
text = sys.stdin.read()
founded = re.findall(Regex_pattern, text, re.S|re.M)
for f in founded:
    f = re.sub(r'\n\s+', r'\n', f)
    print(f)
