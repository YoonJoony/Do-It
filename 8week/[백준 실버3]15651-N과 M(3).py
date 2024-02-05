def dfs(depth):
    if depth == M:
        print(*result)
        return

    for i in range(1, N + 1):
        result.append(i)
        dfs(depth + 1)
        result.pop()


N, M = map(int, input().split())
result = []
dfs(0)
