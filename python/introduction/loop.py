'''
Task
Read an integer NN. For all non-negative integers i<Ni<N, print i2i2.
See the sample for details.
Input Format
The first and only line contains the integer, NN.
Constraints
1 <= N <= 20
Output Format
Print NN lines, one corresponding to each ii.
Sample Input
5
Sample Output
0
1
4
9
16
'''
N = int(raw_input())
for x in xrange(N):
    if x < N:
        print x*x
