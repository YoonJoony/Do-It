import copy

N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
result = 0


def queen_move(x, y, g):
    graph2 = [arr[:] for arr in g]
    graph2[x][y] = 2
    cnt = 0
    for i in range(8):
        mx = x + dx[i]
        my = y + dy[i]
        while True:
            if mx < 0 or mx >= N or my < 0 or my >= N:
                break

            if graph2[mx][my] == 2:
                cnt -= 1
                break

            graph2[mx][my] = 1
            mx += dx[i]
            my += dy[i]

        cnt += 1

    if cnt == 8:
        return graph2
    else:
        return 0


def dfs(n, lst, g):
    global result

    if n == 8:
        if len(lst) == 8:
            result += 1
        return
    prev1, prev2 = -1, -1

    for i in range(0, N):
        for j in range(0, N):
            if not visited[i][j] and g[i][j] < 1 and prev1 != i and prev2 != j:
                visited[i][j] = True
                let = queen_move(i, j, g)
                prev1, prev2 = i, j

                if let != 0:
                    dfs(n + 1, lst + [[i, j]], let)
                elif let == 0:
                    dfs(n, lst, g)

                visited[i][j] = False


prev = [[-1, -1]]
dfs(0, [], graph)

print(result)
