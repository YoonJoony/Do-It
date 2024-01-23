import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

R, C = map(int, input().split())

graph = [list(str(input().rstrip('\n'))) for _ in range(R)]

j_queue = deque([])
f_queue = deque([])

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':  # 지훈이 위치 저장
            j_queue.append((i, j))
            graph[i][j] = 0
        if graph[i][j] == 'F':  # 불 위치 저장
            f_queue.append((i, j))
        if graph[i][j] == '.':
            graph[i][j] = 0  # 이동 비용을 저장 해주기 위해 0으로 변환

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph):
    # 지훈이 위치가 저장된 큐 or 불 위치 저장된 큐가 값이 있으면 계속 돔
    while j_queue or f_queue:
        j_arr = []  # while 한 번 돌 때마다 큐에 있는 좌표를 모두 덜어내고 큐에 새로운 좌표를 추가 해주기 위해 좌표를 임시 저장하는 리스트
        f_arr = []
        # 큐에 저장된 수 만큼 반복 (끝나면 큐는 값이 비게 됨)
        for i in range(len(j_queue)):
            x, y = j_queue.popleft()
            if graph[x][y] != 'F':  # 지훈이가 불에 타죽지 않았을 경우
                if (x == 0 or x == R - 1 or y == 0 or y == C - 1) and graph[x][y] != 'F':  # 가장자리면 탈출
                    return graph[x][y]

                for i in range(4):
                    mx = x + dx[i]
                    my = y + dy[i]
                    if mx < 0 or mx >= R or my < 0 or my >= C:
                        continue
                    if graph[mx][my] == 0:  # 이동할 수 있으면
                        j_arr.append((mx, my))  # 임시 좌표 저장 리스트에 좌표 저장
                        graph[mx][my] = graph[x][y] + 1  # 다음 좌표의 이동 비용을 저장
        # 좌표가 임시 저장된 리스트 수 만큼
        for i in range(len(j_arr)):
            j_queue.append(j_arr[i]) # 큐에 좌표를 전부 새로 추가함.

        # 1턴 불 4방향 확산. (방식은 위랑 똑같음)
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

    return -1  # 두 큐 모두 값이 비어지면 -1 리턴


result = bfs(graph)
if result == -1: # 지훈이가 탈출 못 했을 경우
    print("IMPOSSIBLE")
else:  # 탈출 했을 경우
    print(result + 1)
