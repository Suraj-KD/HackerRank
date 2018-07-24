'''
Task:
You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format:
A single line containing the space-separated integers.

Constraints
1 <= each_integer <= 3

Output Format:
First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

Sample Input:
3 3 3

Sample Output:
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
'''
import numpy


if __name__ == '__main__':
    num = list(map(int, input().strip().split()))
    print(numpy.zeros(num, dtype = numpy.int))
    print(numpy.ones(num, dtype = numpy.int))
