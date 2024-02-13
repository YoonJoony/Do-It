import sys

input = sys.stdin.readline


def dfs(n, arr):
    if result and arr == result[-1]:
        return

    if len(arr) == M:
        result.append(arr)
        return

    for i in range(0, N):
        if not visited[i]:
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