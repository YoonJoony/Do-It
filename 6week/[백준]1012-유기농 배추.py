import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[0 for c in range(N)] for v in range(M)]
result = 0
for _ in range(K):
    n2, n1 = map(int, input().split())
    graph[n1][n2] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque([(x, y)])
    graph[x][y] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= N or my < 0 or my >= M:
                continue
            if graph[mx][my] == 1:
                queue.append((mx, my))
                graph[mx][my] = -1


for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(graph, i, j)
            print(i, j)
            result += 1

print(result)
