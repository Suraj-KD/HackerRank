import sys
INP = sys.stdin.readlines()[1:]
marks = [map(float, x.strip().split()) for x in INP]
final = zip(*marks)
for i in final:
    print(sum(i)/len(i))
