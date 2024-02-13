import sys

input = sys.stdin.readline


def dfs(n, arr):
    if len(arr) == M:
        result.append(arr)
        return
    prev = 0
    for i in range(0, N):
        if not visited[i] and prev != lst[i]:
            prev = lst[i]
            visited[i] = True
            dfs(n + 1, arr + [lst[i]])
            visited[i] = False


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = []
visited = [False for _ in range(N)]

dfs(0, [])

for val in result:
    print(*val)