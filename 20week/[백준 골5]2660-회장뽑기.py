from collections import deque

N = int(input())
lst = [[] for _ in range(N + 1)]
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
weight_lst = []  # 모든 인원의 점수 리스트
min_weight_lst = []  # 최소 점수를 가인 인원의 리스트

while True:
    f1, f2 = map(int, input().split())
    if f1 == -1 and f2 == -1:
        break
    lst[f1].append(f2)
    lst[f2].append(f1)

for i in range(1, N + 1):  # 1 ~ N번 사람까지 각 사람마다 자신을 제외한 다른 사람들의 관계 점수를 계산
    visited = [0] * (N + 1)
    visited[i] = 1
    queue = deque([i])  # (탐색 현 위치, [탐색할 위치의 노드들])
    while queue:
        x = queue.popleft()
        for val in lst[x]:
            if not visited[val]:
                graph[i][val] = graph[i][x] + 1  # 탐색 한 위치 가중치는 => 현 위치의 노드 가중치 + 1
                queue.append(val)
                visited[val] = 1
    weight_lst.append(max(graph[i]))

score = min(weight_lst)  # 점수들 중 최소 점수

for i in range(N):
    if weight_lst[i] == score:  # 최소 점수인 사람을 배열에 넣음
        min_weight_lst.append(i + 1)

print(score, len(min_weight_lst))  # 최소 점수와 최소 점수를 가진 사람 수 출력
print(*min_weight_lst)  # 최소 점수를 가진 사람을 출력
