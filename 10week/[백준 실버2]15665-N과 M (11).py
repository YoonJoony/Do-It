import sys

input = sys.stdin.readline

def dfs(n):
    if n == M:
        print(*result)
        return

    prev = 0
    for i in range(0, N):
        if prev != arr[i]:
            result.append(arr[i])
            prev = arr[i]
            dfs(n + 1)
            result.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

dfs(0)
