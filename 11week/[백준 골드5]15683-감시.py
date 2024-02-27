import itertools
from itertools import combinations
from collections import deque

# 1감은 4번, 2감은 2번, 3, 4감은 4번, 5감은 1번 감시할 수 있는 경우의 수가 존재.

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 감시 카메라 범위 좌표
lst = [0] * 6

dx1 = [[1], [0], [-1], [0]]
dy1 = [[0], [1], [0], [-1]]

dx2 = [[0, 0], [1, -1]]
dy2 = [[1, -1], [0, 0]]

dx3 = [[1, 0], [0, -1], [-1, 0], [0, 1]]
dy3 = [[0, 1], [1, 0], [0, -1], [-1, 0]]

dx4 = [[0, 1, 0], [1, 0, -1], [0, -1, 0], [1, 0, -1]]
dy4 = [[-1, 0, 1], [0, 1, 0], [-1, 0, 1], [0, -1, 0]]

dx5 = [[1, 0, -1, 0]]
dy5 = [[0, 1, 0, -1]]

# 모든 감시 카메라 범위 리스트
all_dx = [0, dx1, dx2, dx3, dx4, dx5]
all_dy = [0, dy1, dy2, dy3, dy4, dy5]

# 감시 카메라 조합 배열
products_dx = []
products_dy = []

camera_q = deque([[] for _ in range(6)])

for i in range(N):
    for j in range(M):
        if 0 < graph[i][j] < 6:
            lst[graph[i][j]] += 1
            camera_q[graph[i][j]].append([i, j])


# 감시 카메라 범위 조합 생성
def products_camera(l):
    global products_dx, products_dy
    for i in range(1, len(l)):
        for j in range(lst[i]):
            products_dx.append(all_dx[i])
            products_dy.append(all_dy[i])

    products_dx = list(itertools.product(*products_dx))
    products_dy = list(itertools.product(*products_dy))


def bfs(g):
    for l in range(len(products_dx)):
        for i in range(1, 6):
            if camera_q[i]:
                for j, val in enumerate(camera_q[i]):
                    x = val[0]
                    y = val[1]

                    if i == 2:

                        mx1 = x + products_dx[l][j][0]
                        my1 = y + products_dy[l][j][0]

                        mx2 = x + products_dx[l][j][1]
                        my2 = y + products_dy[l][j][1]
                        print(mx1, my1)
                        print(mx2, my2)


                        if mx1 == mx2:
                            q1 = deque([(mx1, my1)])
                            q2 = deque([(mx2, my2)])

                            while q1 or q2:
                                v1 = q1.popleft()
                                v2 = q2.popleft()

                                x1, x2= v1[0], v2[0]
                                y1, y2 = v1[1], v2[1]

                                if 0 <= x1 < N and 0 <= y1 < M or graph[x1][y1] == 0:
                                    graph[x1][y1] = "#"
                                    q1.append(x1, y1)



                        elif my2 == my2:



                    # elif i == 5:
                    #     mx = []
                    #     my = []
                    #     for k in range(4):
                    #         mx.append([x + products_dx[5][k]])
                    #         my.append([y + products_dy[5][k]])
                    #     print(mx)
                    #     print(my)




products_camera(lst)
bfs(graph)
print(products_dx[0])
print(camera_q)
