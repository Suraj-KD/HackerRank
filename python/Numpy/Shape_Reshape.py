'''
Task:
You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

Input Format:
A single line of input containing 9 space separated integers.

Output Format:
Print the 3X3 NumPy array.

Sample Input:
1 2 3 4 5 6 7 8 9

Sample Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
import numpy

if __name__ == '__main__':
    arr = numpy.array(input().strip().split(), int)
    arr = numpy.reshape(arr, (3,3))
    print(arr)
