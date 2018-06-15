'''
INPUT: 17 05 2018
OUTPUT: THURSDAY
'''
import sys
import calendar


def calmod(month, day, year):
    """Function to find Day name"""
    return calendar.day_name[calendar.weekday(year, month, day)].upper()


def main():
    """main fuction"""
    print(calmod(*[int(x) for x in sys.stdin.read().strip().split()]))


if __name__ == '__main__':
    main()
