from collections import defaultdict
import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    d = defaultdict(int)
    N = int(input())
    for _ in range(N):
        clothes, body = input().split()
        d[body] += 1

    cnt = 1
    for key in d:
        cnt *= (d[key] + 1)

    print(cnt - 1)
