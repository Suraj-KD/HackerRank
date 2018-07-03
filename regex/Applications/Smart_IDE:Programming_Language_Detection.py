'''
We are trying to hack together a smart programming IDE. Help us build a feature which auto-detects the programming language, given the source code. There are only three languages which we are interested in "auto-detecting": Java, C and Python.

We will provide you with links to a few short or medium size programs for Java, C and Python. In case you aren't familiar with some of these languages, these samples will help you make observations about the lexical structure and syntax of these programming languages. These sample programs are only for your manual inspection. You cannot read or access these sample-programs from the code you submit.

After this, you will be provided with tests, where you are provided the source code for programs - or partial code snippets, but you do not know which language they are in. For each test, try to detect which language the source code is in.

You might benefit from using regular expressions in trying to detect the lexical structure and syntax of the programs provided.

Sample Programs to Understand the Lexical Structure of different Programming Languages

Sample Programs and Code Snippets in C

Sample Programs and Code Snippets in Java

Sample Programs and Code Snippets in Python

INPUT FORMAT:
Source code of a program, or a code snippet, which might be in C, Java or Python.

OUTPUT FORMAT:
Just one line containing the name of the Programming language which you have detected: This might be either C or Java or Python.

SAMPLE INPUT:
import java.io.*;

public class SquareNum {

   public static void main(String args[]) throws IOException
   {
      System.out.println("This is a small Java Program!");
   }
}

SAMPLE OUTPUT:
Java
'''
import re, sys

if __name__ == '__main__':
    Code_snippet = sys.stdin.readlines()
    Regex_pattern_Java = re.compile(r'.*import java\..*')
    Regex_pattern_C = re.compile(r'.*#include<.*')
    matched = False
    for line in Code_snippet:
        if  re.search(Regex_pattern_C, line):
            print("C")
            matched = True
            break
        elif re.search(Regex_pattern_Java, line):
            print("Java")
            matched = True
            break
    if matched == False:
        print("Python")
