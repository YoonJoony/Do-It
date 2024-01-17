import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
linked_node = 0 # 연결 요소의 개수

for _ in range(1, M + 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False for c in range(N + 1)]

# i = 노드 전체를 순회하기 때문에 순회 하는 배열 위치
# i위치 노드에 연결된 모든 노드를 bfs를 통해 모드 방문하여 True로 만듬.
# 그러면 i+n번째에 방문이 안 되었다는건 연결된게 없거나 or 다른 곳과 연결되있다는 뜻.
# 따라서 밑에 33번줄 for문으로 0부터 돌며 연결 요소를 찾으면 1 증감 시키면서 순회하면
# 전체 연결 요소의 개수가 나온다.
def bfs(graph, i):
    queue = deque([i])
    visited[i] = True

    while queue:
        v = queue.popleft()
        for val in graph[v]:
            if not visited[val]:
                visited[val] = True
                queue.append(val)

# 노드 전체를 순회하면서 방문
for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, i)
        linked_node += 1

print(linked_node)
