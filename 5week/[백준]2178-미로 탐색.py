import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip('\n'))) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [1, -1]
dy = [1, -1]
result = []
count = 1 # 거리 카운트


def dfs(y, x, graph):
    visited[y][x] = True
    global dx, dy, count
    if y == N - 1 and x == M - 1:
        visited[y][x] = False
        result.append(count)

    if graph[y][x] == 1:
        # 상하좌우 1인 수 찾기위해 dx, dy값 활용
        for i in range(2):
            mx = x + dx[i] # 이동시킬 좌표
            my = y + dy[i]

            # 마지막 좌표가 아니면서 이동할 좌표가 범위를 벗어나지 않으면서 노드를 방문 안헀을 시
            if (y != N - 1 or x != M - 1) and 0 <= mx < M and graph[y][mx] == 1 and not visited[y][mx]:
                count += 1
                dfs(y, mx, graph)
            if (y != N - 1 or x != M - 1) and 0 <= my < N and graph[my][x] == 1 and not visited[my][x]:
                count += 1
                dfs(my, x, graph)
    # 위 재귀함수 호출 후 재귀될 때 거리를 다시 원상 복구하여 1씩 줄인다.
    count -= 1


dfs(0, 0, graph)
print(min(result))