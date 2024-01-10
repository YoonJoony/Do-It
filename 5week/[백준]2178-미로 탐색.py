import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip('\n'))) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [1, -1]
dy = [1, -1]
result = []
count = 1


def dfs(y, x, graph):
    visited[y][x] = True
    global dx, dy, count

    if y == N - 1 and x == M - 1:
        visited[y][x] = False
        result.append(count)

    if graph[y][x] == 1:
        for i in range(2):
            mx = x + dx[i]
            my = y + dy[i]

            if (y < N - 1 or x < M - 1) and 0 <= mx < M and graph[y][mx] == 1 and not visited[y][mx]:
                count += 1
                dfs(y, mx, graph)
            if (y != N - 1 or x != M - 1) and 0 <= my < N and graph[my][x] == 1 and not visited[my][x]:
                count += 1
                dfs(my, x, graph)
    count -= 1


dfs(0, 0, graph)
print(min(result))