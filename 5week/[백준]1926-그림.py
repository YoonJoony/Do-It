import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

result = [0] # 그림 카운트한 결과 저장 배열(그림 개수만큼)
count = 0 # 그림 카운트 변수
def dfs(y, x, graph):
    global visited, count
    visited[y][x] = True
    dx = [1, -1]
    dy = [1, -1]
    if graph[y][x] == 1: # 현재 좌표의 값이 1일 경우
        count += 1 # 그림 크기 카운트
        for i in range(2):
            mx = x + dx[i] # x좌표 좌우
            my = y + dy[i] # y좌표 좌우
            if 0 <= mx < M and graph[y][mx] == 1 and not visited[y][mx]:
                # 재귀 함수를 통해 좌표를 이동한 값이 1이 안될 때까지 재귀 및 반복
                dfs(y, mx, graph)
            if 0 <= my < N and graph[my][x] == 1 and not visited[my][x]:
                dfs(my, x, graph)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j, graph)
            result.append(count)
            count = 0

print(len(result) - 1)
print(max(result))
