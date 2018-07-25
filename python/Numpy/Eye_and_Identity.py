'''
Task:
Your task is to print an array of size NXM with its main diagonal elements as 1's and 0's everywhere else.

Input Format:
A single line containing the space separated values of N and M.
N denotes the rows.
M denotes the columns.

Output Format:
Print the desired NXM array.

Sample Input:
3 3

Sample Output:
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
'''
import numpy


if __name__ == '__main__':
    X, Y = tuple(map(int, input().strip().split()))
    print(str(numpy.eye(X, Y)).replace("1", " 1").replace("0", " 0"))
