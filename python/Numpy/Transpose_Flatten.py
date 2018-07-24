'''
Task:
You are given a NXM integer array matrix with space separated elements (N = rows and M = columns). 
Your task is to print the transpose and flatten results.

Input Format:
The first line contains the space separated values of N and M. 
The next  lines contains the space separated elements of M columns.

Output Format:
First, print the transpose array and then print the flatten.

Sample Input:
2 2
1 2
3 4

Sample Output:
[[1 3]
 [2 4]]
[1 2 3 4]
'''
import numpy
import sys

if __name__ == '__main__':
    arr = list()
    inp = sys.stdin.readlines()[1:]
    for i in inp:
        arr.append(i.strip().split())
    arr = numpy.array(arr, int)
    print(numpy.transpose(arr))
    print(arr.flatten())
