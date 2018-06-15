import sys
def make_dir(lst):
    student = dict()
    student[lst[0]] = format(sum(map(float, lst[1:]))/float(len(lst)-1), '.2f')
    return student
if __name__ == '__main__':
    N = int(input())
    records = dict()
    input_list= sys.stdin.readlines()
    query_name = input_list[-1]
    lines = [x.strip() for x in input_list[:N]]
    for line in lines:
        record = make_dir(line.split(' '))
        records.update(record)
    print(records[query_name])
