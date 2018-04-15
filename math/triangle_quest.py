'''
You are given a positive integer N.
Print a numerical triangle of height N - 1 like the one below:
1
22
333
4444
Input:
A single line containing integer N.
like 4
Output:
triangle mentioned above
like:
1
22
333
'''
for i in range(1, int(raw_input())):
    print i*(10**i-1)/9
