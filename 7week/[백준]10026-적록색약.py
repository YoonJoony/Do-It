import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
original_graph = [list(_ for _ in str(input().rstrip('\n'))) for _ in range(N)]
blindness_graph = [['R' if color == 'G' else color for color in row] for row in original_graph]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y, visited):
    visited[x][y] = True
    queue = deque([(x, y)])
    rgb = graph[x][y]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue

            if graph[mx][my] == rgb and not visited[mx][my]:
                queue.append((mx, my))
                visited[mx][my] = True


def count_areas(graph):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(graph, i, j, visited)
                cnt += 1
    return cnt


not_blindness = count_areas(original_graph)
blindness = count_areas(blindness_graph)

print(not_blindness, blindness)

# import sys
# from collections import deque
# sys.setrecursionlimit(10 ** 6)
#
# N = int(input())
# graph = [list(_ for _ in str(input().rstrip('\n'))) for _ in range(N)]
#
# visited = [[False for _ in range(N)] for _ in range(N)]
# blindness_visited = [[False for _ in range(N)] for _ in range(N)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# cnt = 0
# blindness_cnt = 0
#
# def bfs(graph, x, y, flag, v):
#     v[x][y] = True
#     queue = deque([(x, y)])
#     rgb = graph[x][y]
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             mx = x + dx[i]
#             my = y + dy[i]
#             if mx < 0 or mx >= N or my < 0 or my >= N:
#                 continue
#             xy_rgb = graph[mx][my]
#
#             if flag:
#                 if xy_rgb == 'R' and rgb == 'G':
#                     xy_rgb = 'G'
#                 elif xy_rgb == 'G' and rgb == 'R':
#                     xy_rgb = 'R'
#
#             if xy_rgb == rgb and not v[mx][my]:
#                 queue.append((mx, my))
#                 v[mx][my] = True
#
#
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             bfs(graph, i, j, False, visited)
#             cnt += 1
#         if not blindness_visited[i][j]:
#             bfs(graph, i, j, True, blindness_visited)
#             blindness_cnt += 1
#
# print(cnt, blindness_cnt)
