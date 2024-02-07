import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def function(sm, n):
    if n == 1:
        return 10

    while st:




A, B, C = map(int, input().split())
result = function(A, B) % C
st = deque([A])
print(result)
