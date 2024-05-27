from collections import deque

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
weight_lst = []  # 모든 인원의 점수 리스트

for _ in range(M):
    f1, f2 = map(int, input().split())
    lst[f1].append(f2)
    lst[f2].append(f1)

for i in range(1, N + 1):
    graph = [0 for _ in range(N + 1)]
    visited = [0] * (N + 1)
    visited[i] = 1
    queue = deque([(i, lst[i])])  # (탐색 현 위치, [탐색할 위치의 노드들])
    while queue:
        tp = queue.popleft()
        here = tp[0]  # 탐색 현 위치
        v = tp[1]  # 탐색할 위치의 노드들
        for val in v:
            if not visited[val]:
                graph[val] = graph[here] + 1  # 탐색 한 위치 가중치는 => 현 위치의 노드 가중치 + 1
                queue.append((val, lst[val]))
                visited[val] = 1
    weight_lst.append(sum(graph))

print(weight_lst.index(min(weight_lst)) + 1)
