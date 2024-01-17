N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(x, y):
    # x,y 좌표가 그래프 공간을 벗어나면 False
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True 
    return False


cnt = 0
result = []
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result.append(cnt)
            cnt = 0

print(len(result))
print(max(result) if result else 0)