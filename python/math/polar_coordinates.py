'''
Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
A complex number is completely determined by its real part  and imaginary part .
If we convert complex number  to its polar coordinate, we find:
: Distance from  to origin, i.e.,
: Counter clockwise angle measured from the positive -axis to the line segment that joins  to the origin.
Python's cmath module provides access to the mathematical functions for complex numbers.
Task
You are given a complex . Your task is to convert it to polar coordinates.
Input Format
A single line containing the complex number .
Note: complex() function can be used in python to convert the input as a complex number.
Constraints
Given number is a valid complex number
Output Format
Output two lines:
The first line should contain the value of .
The second line should contain the value of .
Sample Input
1+2j
Sample Output
2.23606797749979
1.1071487177940904
Note: The output should be correct up to 3 decimal places.
'''
from cmath import  sqrt, phase
Z = complex(input("Enter one complex number : "))
print sqrt(pow(Z.real, 2)+pow(Z.imag, 2)).real
print phase(complex(Z.real, Z.imag))
