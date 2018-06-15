import sys

def pyeval(comm):
    eval(comm)
    
    
def main():
    pyeval(sys.stdin.read())
    
    
if __name__ == '__main__':
    main()
