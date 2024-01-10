import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
M = int(input())
count = 0
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (N + 1)


def dfs(graph, v, visited):
    visited[v] = True
    global count
    count += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(count-1)