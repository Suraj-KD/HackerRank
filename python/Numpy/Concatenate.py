'''
Task:
You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

Input Format:
The first line contains space separated integers N, M and P. 
The next N lines contains the space separated elements of the  columns. 
After that, the next M lines contains the space separated elements of the P columns.

Output Format:
Print the concatenated array of size (N + M)XP.

Sample Input:
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4

Sample Output:
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
'''
import numpy


if __name__ == '__main__':
    arr1 = list()
    arr2 = list()
    N, M, P = input().strip().split()
    for _ in range(1,int(N)+1):
        arr1.append(input().strip().split())
    arr1 = numpy.array(arr1, int)
    for _ in range(1,int(M)+1):
        arr2.append(input().strip().split())
    arr2 = numpy.array(arr2, int)
    print(numpy.concatenate((arr1, arr2), axis=0))
