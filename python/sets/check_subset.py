import sys

def issub(a, b):
    return set(a).issubset(set(b))

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()]
    for i in range(lines[0][0]):
        print(issub(lines[2 + 4*i], lines[4 + 4*i]))

if __name__ == '__main__':
    main()
