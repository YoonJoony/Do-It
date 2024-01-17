import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().rstrip('\n'))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

complex_count = 0 # 단지 카운트
apart = [] # 집 개수 저장할 배열
apart_count = 0 # 집 개수 카운트


def bfs(graph, x, y):
    global apart_count
    queue = deque([(x, y)])
    graph[x][y] = -1

    while queue:
        apart_count += 1  # 집 개수 카운트
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            if graph[mx][my] == 1:
                queue.append((mx, my))
                graph[mx][my] = -1


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(graph, i, j)
            apart.append(apart_count)  # 집 카운트 추가
            apart_count = 0
            complex_count += 1

apart.sort()
print(complex_count)
print('\n'.join(map(str, apart)))
