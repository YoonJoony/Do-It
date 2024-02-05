def dfs(start, depth):
    if depth == M:
        print(*result)
        return

    for j in range(start, N + 1):
        result.append(j)
        dfs(j + 1, depth + 1)
        result.pop()


N, M = map(int, input().split())
result = []
dfs(1, 0)
