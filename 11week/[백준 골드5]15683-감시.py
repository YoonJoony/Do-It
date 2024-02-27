import itertools
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

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
# 위 모든 감시 카메라 범위 리스트
all_dx = [0, dx1, dx2, dx3, dx4, dx5]
all_dy = [0, dy1, dy2, dy3, dy4, dy5]

# 감시 카메라 조합 배열
products_dx = []
products_dy = []
# 감시 카메라 범위 좌표
lst = [0] * 6
result = float('inf')  # 결과 저장할 변수

# 감시 카메라 번호마다 개수 저장.
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


# 감시 범위를 확장 (x, y) : 현재 카메라 위치, (dx, dy) : 확장될 감시 카메라 방향, g : 그래프
def expand_watch_area(x, y, dx, dy, g):
    q = deque([(x + dx, y + dy)]) # 카메라 방향 으로 한 칸 이동한 좌표
    while q:
        x, y = q.popleft()
        if 0 <= x < N and 0 <= y < M and g[x][y] != 6:
            g[x][y] = '#'
            q.append((x + dx, y + dy))


def bfs(g):
    global result
    # 감시 카메라 조합 개수 만큼 반복
    for l in range(len(products_dx)):
        graph2 = [arr[:] for arr in g]  # 조합마다 그래프 원상복구
        flag = 0
        for i in range(1, 6):
            if camera_q[i]:
                for j, val in enumerate(camera_q[i]):
                    x, y = val
                    if i == 1: # 1번 카메라인 경우 한 방향으로만 감시됨
                        expand_watch_area(x, y, products_dx[l][flag][0], products_dy[l][flag][0], graph2)
                    elif i == 2 or i == 3 or i == 4: # (2번, 3번)  카메라인 경우 두 방향으로만 감시됨
                        expand_watch_area(x, y, products_dx[l][flag][0], products_dy[l][flag][0], graph2)
                        expand_watch_area(x, y, products_dx[l][flag][1], products_dy[l][flag][1], graph2)
                        if i == 4:  # 3번 카메라인 경우 세 방향으로만 감시됨
                            expand_watch_area(x, y, products_dx[l][flag][2], products_dy[l][flag][2], graph2)
                    elif i == 5:  # 4번 카메라인 경우 네 방향으로만 감시됨 -> for 문
                        for _ in range(4):
                            expand_watch_area(x, y, dx5[0][_], dy5[0][_], graph2)
                    flag += 1
        cnt = 0
        for val in graph2:  # 결과 저장
            cnt += val.count(0)
        result = min(result, cnt)


products_camera(lst)
bfs(graph)
print(result)
