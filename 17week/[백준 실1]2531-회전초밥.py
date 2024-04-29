import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
lst = [int(input().strip('\n')) for _ in range(N)]

right = 1
arr = deque([lst[0]])
MAX = float('-inf')
cnt = 1

while True:
    if len(arr) == k:
        temp = set(arr)
        if c not in temp:
            MAX = max(len(temp) + 1, MAX)
        else:
            MAX = max(len(temp), MAX)
        arr.popleft()

    if right == N:
        right = 0
    if cnt == N + k:
        break

    arr.append(lst[right])
    right += 1
    cnt += 1


print(MAX)
