'''
ABCXYZ company has up to 100 employees. 
The company decides to create a unique identification number (UID) for each of its employees. 
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:
 	
It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0-9).
It should only contain alphanumeric characters (a-z , A-Z & 0-9).
No character should repeat.
There must be exactly 10 characters in a valid UID.

Input Format:
The first line contains an integer T, the number of test cases. 
The next T lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input:
2
B1CD102354
B1CDEF2354

Sample Output:
Invalid
Valid
'''
import re


if __name__ == '__main__':
    num_of_line = int(input())
    for _ in range(num_of_line):
        line = input()
        count_U = 0
        count_I = 0
        flag = True
        for c in line:
            if re.match(r'[A-Z]', c):
                count_U += 1
            if re.match(r'[0-9]', c):
                count_I += 1
            m = line.count(c)
            if m > 1:
                flag = False
        if count_I >= 3 and count_U >= 2 and len(line) == 10 and flag:
            print("Valid")
        else:
            print("Invalid")
