import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit_graph = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque([])

cnt = 0
asd = []
asd_rock = True
ripe = True  # 토마토가 전부 익은 여부
riped = False


def bfs(graph):
    global queue, cnt, asd, asd_rock, riped

    while queue:
        x, y, z = queue.popleft()
        visit_graph[x][y][z] = True

        if (x, y, z) == asd and riped:
            cnt += 1
            asd_rock = True

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
                riped = True
        if queue and asd_rock:
            asd = queue[-1]

        asd_rock = False


for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1 and not visit_graph[i][j][k]:
                queue.append((i, j, k))

bfs(graph)

for i in range(H):
    for j in range(N):
        if graph[i][j].count(0) > 0:
            ripe = False

if ripe:
    print(cnt)
else:
    print(-1)
