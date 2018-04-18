'''
Task
Given an integer, n, perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format:
A single line containing a positive integer, n.
Constraints:
1 <= n <= 100
Output Format:
Print Weird if the number is weird; otherwise, print Not Weird.
'''
'''
THIS CODE WORKS  IN PYTHON-3
if __name__ == '__main__':
    N = int(input())
    if n % 2 == 0:
        if (N >= 2 and N <= 5) or N > 20:
            print("Not Weird")
        else:
            print("Weird")
    else:
        print("Weird")
'''
if __name__ == '__main__':
    N = int(raw_input())
    if N % 2 == 0:
        if (N >= 2 and N <= 5) or N > 20:
            print "Not Weird"
        else:
            print "Weird"
    else:
        print "Weird"

