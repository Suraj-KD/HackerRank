'''
Task
You are given a two lists A and B.
Your task is to compute their cartesian product AXB.
Example :
A = [1, 2]
B = [3, 4]
AxB = (1,3) (1, 4) (2, 3) (2, 4)
'''
A = [int(i) for i in raw_input().split()]
B = [int(i) for i in raw_input().split()]
RESULT = [(i, j) for i in A for j in B]
for i in RESULT:
    print i,
