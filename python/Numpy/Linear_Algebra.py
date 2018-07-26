'''
Task:
You are given a square matrix A with dimensions NXN. Your task is to find the determinant.

Input Format:
The first line contains the integer N.
The next N lines contains the N space separated elements of array A.

Output Format:
Print the determinant of A.

Sample Input:
2
1.1 1.1
1.1 1.1

Sample Output:
0.0
'''
import numpy


if __name__ == '__main__':
    N = int(input())
    numpy.set_printoptions(legacy='1.13')
    A = numpy.array([input().split() for _ in range(N)], float)
    print(numpy.linalg.det(A))
