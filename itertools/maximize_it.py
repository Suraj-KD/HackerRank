'''
You are given a function f(X) = X^2.
You are also given K lists.
The ith list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S = (f(X1)+f(X2)+....f(Xk)) % M
Xi denotes the element picked from the ith list .
Find the maximized value Smax obtained.
% denotes the modulo operator.
Note that you need to take exactly one element from each list,
not necessarily the largest element.
You add the squares of the chosen elements and perform the modulo operation.
The maximum value that you can obtain, will be the answer to the problem.
Input Format:
The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the ith list,
followed by Ni space separated integers denoting the elements in the list.
Constraints:
1 <= K <= 7
1 <= M <= 1000
1 <= Ni <= 7 
1 <= Magnitude of the elements  in list <= 10^9
Output Format:
Output a single integer denoting the value Smax.

Sample Input:
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
Sample Output:
206
Explanation:
Picking 5 from the 1st list, 9 from the 2nd list and 10 from and
the 3rd list gives the maximum S value equal to (5^2 + 9^2 + 10^2)%1000 = 206.
'''
'''
Note : THIS CODE WORK IN PYTHON-3
from itertools import product
k, m = tuple(map(int, input().strip().split()))
lists = []
for i in range(k):
    lists.append(list(map(int, input().strip().split()))[1:])
max = 0
for each in product(*lists):
    modu = sum([x**2 for x in each])% m
    if modu > max:
        max = modu
print(max)
'''
from itertools import product
K, M = tuple(map(int, raw_input().strip().split()))
LISTS = []
for i in range(K):
    LISTS.append(list(map(int, raw_input().strip().split()))[1:])
MAX = 0
for each in product(*LISTS):
    MODU = sum([x**2 for x in each])% M
    if MODU > MAX:
        MAX = MODU
print MAX
