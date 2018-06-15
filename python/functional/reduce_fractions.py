from fractions import Fraction
from functools import reduce
def  Product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator

def main():
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = Product(fracs)
    print(*result)

if __name__ == '__main__':
    main()
