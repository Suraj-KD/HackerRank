'''
Program to check that whether a year is leap or not
'''
from __future__ import print_function, division
import sys

def is_leap(year):
    return (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)

def main():
    #year = int(sys.stdin.read().strip()) #This line is used to read input from stdin file
    year = int(raw_input())
    print(is_leap(year))

if __name__ == '__main__':
    main()
