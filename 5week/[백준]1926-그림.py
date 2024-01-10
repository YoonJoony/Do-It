import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

result = [0]
count = 0
def dfs(y, x, graph):
    global visited, count
    visited[y][x] = True
    dx = [1, -1]
    dy = [1, -1]
    if graph[y][x] == 1:
        count += 1
        for i in range(2):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < M and graph[y][mx] == 1 and not visited[y][mx]:
                dfs(y, mx, graph)
            if 0 <= my < N and graph[my][x] == 1 and not visited[my][x]:
                dfs(my, x, graph)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j, graph)
            result.append(count)
            count = 0

print(len(result) - 1)
print(max(result))
