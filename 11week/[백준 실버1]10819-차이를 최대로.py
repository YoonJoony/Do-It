from collections import deque

N = int(input())
lst = list(map(int, input().split()))
visited = [0] * N
result = 0


def dfs(n, arr):
    global result

    if n == N:
        sm = 0
        for k in range(N):
            if k < N - 1:
                sm += abs(arr[k] - arr[k + 1])
        result = max(result, sm)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n + 1, arr + [lst[i]])
            visited[i] = False


dfs(0, [])
print(result)