import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

R, C = map(int, input().split())

graph = [list(str(input().rstrip('\n'))) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

j_queue = deque([])
f_queue = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            graph[i][j] = 0
            x = i
            y = j

        if graph[i][j] == 'F':
            f_queue.append((i, j))

        if graph[i][j] == '.':
            graph[i][j] = 0


def bfs(graph):
    global j_queue, f_queue, x, y

    if x == 0 or x == R - 1 or y == 0 or y == C - 1:
        return 0

    j_queue.append((x, y))
    while j_queue or f_queue:
        if j_queue:
            x, y = j_queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= R or my < 0 or my >= C or graph[mx][my] != 0:
                continue

            if graph[mx][my] == 0 and graph[x][y] != 'F':
                j_queue.append((mx, my))
                graph[mx][my] = graph[x][y] + 1

            if (mx == 0 or mx == R - 1 or my == 0 or my == C - 1) and graph[x][y] != 'F':
                return graph[mx][my]
        if f_queue:
            x, y = f_queue.popleft()
            visited[x][y] = True

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= R or my < 0 or my >= C or graph[mx][my] == '#':
                continue

            if not visited[mx][my]:
                f_queue.append((mx, my))

            graph[mx][my] = 'F'
    return -1


result = bfs(graph)

if result == -1:
    print('IMPOSSIBLE')
else:
    print(result + 1)
