from collections import deque

N, K = map(int, input().split())
lst = list(map(int, input().split()))

v = [0] * (max(lst) + 1)
arr = deque([])

right = 0
MAX = float('-inf')

while right < N:
    if v[lst[right]] >= K:
        MAX = max(len(arr), MAX)
        v[arr.popleft()] -= 1
    else:
        arr.append(lst[right])
        v[lst[right]] += 1
        right += 1
MAX = max(len(arr), MAX)
print(MAX)