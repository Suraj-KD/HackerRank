import sys


def find_execp(a, b):
    try:
        print(int(int(a)//int(b)))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
        

def main():
    a = sys.stdin.readlines()[1:]
    for i in a:
        find_execp(*(i.strip().split(' ')))


if __name__ == '__main__':
    main()
