import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
d = defaultdict(int)
for _ in range(M):
    stNum = str(input().strip('\n'))
    if d[stNum]:
        d.pop(stNum)
    d[stNum] += 1

for val in list(d.keys())[:N]:
    print(val)