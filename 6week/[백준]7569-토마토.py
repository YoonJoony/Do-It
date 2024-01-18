import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit_graph = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(graph, x, y, z):
    queue = deque([(x, y, z)])
    visit_graph[x][y][z] = True

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            mx = x + dx[i]
            my = y + dy[i]
            mz = z + dz[i]

            if mx < 0 or mx >= H or my < 0 or my >= N or mz < 0 or mz >= M:
                continue
            if graph[mx][my][mz] == 0:
                queue.append((mx, my, mz))
                graph[mx][my][mz] = 1
                visit_graph[x][y][z] = True


for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1 and not visit_graph[i][j][k]:
                bfs(graph, i, j, k)

for i in range(H):
    for j in range(N):
        if graph[i][j].count(0) > 0:

print(graph)

