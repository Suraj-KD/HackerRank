def Leftrotate(d, a):
    new_array = [None]*len(a)
    for i in range(len(a)):
        new_array[i-d] = a[i]
    return new_array

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result = Leftrotate(d, a)
    print(' '.join(map(str, result)))
