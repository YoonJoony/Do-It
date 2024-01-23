import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

R, C = map(int, input().split())

graph = [list(str(input().rstrip('\n'))) for _ in range(R)]

j_queue = deque([])
f_queue = deque([])

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            j_queue.append((i, j))
            graph[i][j] = 0
        if graph[i][j] == 'F':
            f_queue.append((i, j))
        if graph[i][j] == '.':
            graph[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph):
    # 지훈이 위치가 저장된 큐 or 불 위치 저장된 큐가 값이 있으면 계속 돔
    while j_queue or f_queue:
        j_arr = []
        f_arr = []

        for i in range(len(j_queue)):
            x, y = j_queue.popleft()
            if graph[x][y] != 'F':
                if (x == 0 or x == R - 1 or y == 0 or y == C - 1) and graph[x][y] != 'F':
                    return graph[x][y]

                for i in range(4):
                    mx = x + dx[i]
                    my = y + dy[i]
                    if mx < 0 or mx >= R or my < 0 or my >= C:
                        continue
                    if graph[mx][my] == 0:
                        j_arr.append((mx, my))
                        graph[mx][my] = graph[x][y] + 1

        for i in range(len(j_arr)):
            j_queue.append(j_arr[i])

        # 1턴 불 4방향 확산
        for i in range(len(f_queue)):
            x, y = f_queue.popleft()
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]

                if mx < 0 or mx >= R or my < 0 or my >= C:
                    continue

                if graph[mx][my] != '#' and graph[mx][my] != 'F':
                    f_arr.append((mx, my))  # 확산된 불 좌표 저장
                    graph[mx][my] = 'F'
        # 확산된 불 좌표 큐에 저장
        for i in range(len(f_arr)):
            f_queue.append(f_arr[i])

    return -1


result = bfs(graph)
if result == -1:
    print("IMPOSSIBLE")
else:
    print(result + 1)
