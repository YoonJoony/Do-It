import sys
from collections import deque

N, M = map(int, input().split())
X, Y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
sm = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global sm, d

    if graph[x][y] == 0:
        graph[x][y] = 2
        sm += 1

    flag = 0

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or mx >= N or my < 0 or my >= M:
            continue

        if graph[mx][my] == 0:
            flag = 1
            break

    if flag == 1:
        for i in range(1, 5):
            mx = x + dx[d - i]
            my = y + dy[d - i]

            if mx < 0 or mx >= N or my < 0 or my >= M:
                continue

            if graph[mx][my] == 0:
                if (d - i) < 0:
                    d = (d - i) + 4
                else:
                    d = d - i

                dfs(mx, my)
    else:
        mx = x + dx[d - 2]
        my = y + dy[d - 2]

        if mx < 0 or mx >= N or my < 0 or my >= M or graph[mx][my] == 1:
            print(sm)
            sys.exit(0)

        dfs(mx, my)


dfs(X, Y)
