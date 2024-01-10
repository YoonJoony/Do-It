import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]

for i in range(1, M + 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)

print(graph)
# DFS 구현
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, V, visited)

print()

# BFS 구현
def bfs(graph, start, visited):
    global queue
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


queue = deque([V])
visited = [False] * (N + 1)
bfs(graph, V, visited)
