import sys, re


def validate_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error as e:
        return False


    
def main():
    for i in sys.stdin.readlines()[1:]:
        print(validate_regex(i))

        
if __name__ == '__main__':
    main()
