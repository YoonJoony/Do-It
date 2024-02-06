def dfs(depth):
    if depth == M:
        print(*result)
        return

    for i in range(0, N):
        if not visited[i]:
            result.append(arr[i])
            visited[i] = True
            dfs(depth + 1)
            result.pop()
            visited[i] = False


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False for _ in range(N)]
result = []
dfs(0)
