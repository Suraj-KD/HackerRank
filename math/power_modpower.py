'''
So far, we have only heard of Python's powers. Now, we will witness them!
Powers or exponents in Python can be calculated using the built-in power function.
pow(a, b)
It is also possible to calculate  a to-the-power b mod m.
like pow(a, b, m)
This is very helpful in computations where you have to print the resultant % mod.
Note: Here, a and b can be floats or negatives,
but, if a third argument is present, b cannot be negative.
Note: Python has a math module that has its own pow().
It takes two arguments and returns a float.
Frankly speaking, we will never use math.pow().
Task
You are given three integers: , , and , respectively. Print two lines.
The first line should print the result of pow(a,b).
The second line should print the result of pow(a,b,m).
Input Format
The first line contains , the second line contains , and the third line contains.
Constraints
1 <= a <= 10
1 <= b <= 10
2 <= m <= 1000
Sample Input
3
4
5
Sample Output
81
1
'''
A = int(raw_input())
B = int(raw_input())
M = int(raw_input())
print pow(A, B)
print pow(A, B, M)
