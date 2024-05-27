from collections import deque
import sys

input = sys.stdin.readline

# 노드의 개수 입력
N = int(input())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 그래프 입력
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모를 저장할 리스트 초기화
parent = [0] * (N + 1)

# BFS 함수 정의
def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if parent[neighbor] == 0:
                parent[neighbor] = node
                queue.append(neighbor)

# 1번 노드에서 BFS 시작
bfs(1)

# 2번 노드부터 부모 출력
for i in range(2, N + 1):
    print(parent[i])
