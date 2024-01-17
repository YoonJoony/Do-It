import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip('\n'))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph):
    global cnt
    graph[0][0] = 0
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= N or my < 0 or my >= M:
                continue

            if graph[mx][my] == 1:
                graph[mx][my] += graph[x][y]
                queue.append((mx, my))


bfs(graph)
print((graph[N-1][M-1] + 1))