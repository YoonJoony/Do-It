import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

for _ in range(int(input())):
    l = int(input())
    graph = [[0 for _ in range(l)] for _ in range(l)]

    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    x, y = map(int, input().split())
    ex, ey = map(int, input().split())


    def bfs(graph):
        global x, y, ex, ey

        if x == ex and y == ey:
            return

        graph[ex][ey] = -1
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            for i in range(8):
                mx = x + dx[i]
                my = y + dy[i]

                if mx < 0 or mx >= l or my < 0 or my >= l:
                    continue
                if graph[mx][my] == -1:
                    graph[mx][my] = graph[x][y] + 1
                    return
                elif graph[mx][my] == 0:
                    queue.append((mx, my))
                    graph[mx][my] = graph[x][y] + 1

    bfs(graph)
    print(graph[ex][ey])
