cube = lambda x:x**3 # complete the lambda function 


def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    if n <= 0:
        fib_list = []
    if n == 1:
        fib_list = fib_list[:n]
    return fib_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
