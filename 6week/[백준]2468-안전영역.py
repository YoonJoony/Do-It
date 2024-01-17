import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
precipitation = 0  # 강수량 저장 변수
graph = []

safe_area = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    precipitation = max(graph[i])  # 가장 큰 건물 -1 만큼 강수량의 안전영역을 조사해야 하기 때문에
    # 강수량 변수에 가장 큰 건물의 높이만큼 저장함.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y, p):
    queue = deque([(x, y)])
    visit_graph[x][y] = True  # 현재 좌표의 값을 변경시켜주는 다른 BFS 문제와 달리 강수량 만큼 다시
    # 그래프를 돌려야 하기 때문에 그래프를 매번 다시 만드는 것 보다
    # 방문 여부 좌표를 하나 더 만드는게 낫다.

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            if graph[mx][my] > p and not visit_graph[mx][my]:  # 안전 영역일 경우 조건
                visit_graph[mx][my] = True
                queue.append((mx, my))


for p in range(precipitation):  # 강수량 크기 만큼 돌림
    safe_area_count = 0  # 강수량 돌릴 때마다 안전영역 크기 0으로 초기화

    visit_graph = [[False for _ in range(N)] for _ in range(N)]  # 방문 배열도 초기화

    # BFS 시작
    for i in range(N):
        for j in range(N):
            if graph[i][j] > p and not visit_graph[i][j]:  # 안전영역일 경우 and 방문 안했을 경우
                bfs(graph, i, j, p)
                safe_area_count += 1  # 안전영역 집합 카운트
    safe_area.append(safe_area_count)  # 안전영역 개수 집어 넣음

print(max(safe_area))  # 안전 영역 최대값 출력
