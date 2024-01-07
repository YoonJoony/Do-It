import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] * N for _ in range(N + 1)]

for i in range(1, M + 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n1].sort()

visited = [False] * (N+1)

# DFS 구현
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    if not graph[v]:
        v2 = v
        for i in range(1, N+1):
            if graph[i].count(v) != 0 and not visited[i]:
                v2 = i

        if not visited[v2]:
            visited[v2] = True
            print(v2, end=" ")

        for i in graph[v2]:
            if not visited[i]:
                dfs(graph, i, visited)
    else:
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

dfs(graph, V, visited)

print("\n", end="")

# BFS 구현
def bfs(graph, start, visited):
    visited = [False] * (N+1)

    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

        if not graph[v]:
            for i in range(1, N+1):
                if graph[i].count(v) != 0 and not visited[i]:
                    visited[i] = True
                    queue.append(i)


bfs(graph, V, visited)