import sys

input = sys.stdin.readline


def dfs(n):
    if n == M:
        print(*result)
        return

    for i in range(0, N):
        result.append(lst[i])
        dfs(n + 1)
        result.pop()


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []

dfs(0)
