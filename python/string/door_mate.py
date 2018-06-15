from __future__ import print_function
import sys

def design(R, C):
    lines = list()

    for n in range(1, R//2 + 1):
        line = ('.|.' * (n*2-1)).center(C, '-')
        lines.append(line)

    lines.append('WELCOME'.center(C, '-'))
    lines.extend(reversed(lines[:-1]))
    return lines

def main():
    N, M = [ int(x) for x in sys.stdin.read().strip().split()[:2] ]
    for line in design(N, M):
        print(line)

if __name__ == '__main__':
    main()

