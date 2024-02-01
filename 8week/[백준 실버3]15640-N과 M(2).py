import sys
from collections import deque

n, m = map(int, input().split())
queue = deque([])

for i in range(1, n + 1):
    queue.append(i)


def n_and_m(x, n, m):


    for i in range(m):
        print(x + 1, end=" ")
    n_and_m(x+1, n, m)


n_and_m(0, n, m)
