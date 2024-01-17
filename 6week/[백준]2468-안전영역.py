import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
precipitation = 0
graph = []

safe_area = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    precipitation = max(graph[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y, p):
    queue = deque([(x, y)])
    visit_graph[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            if graph[mx][my] > p and not visit_graph[mx][my]:
                visit_graph[mx][my] = True
                queue.append((mx, my))


for p in range(precipitation):
    safe_area_count = 0

    visit_graph = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] > p and not visit_graph[i][j]:
                bfs(graph, i, j, p)
                safe_area_count += 1
    safe_area.append(safe_area_count)

print(max(safe_area))