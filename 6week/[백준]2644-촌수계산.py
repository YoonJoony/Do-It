import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())
cnt = 0
result_flag = False

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
# 시작 노드(A)를 기준으로 노드마다 A의 촌수를 저장하는 배열.
result_graph = [0 for _ in range(N + 1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

queue = deque([A])


def bfs(graph):
    global queue
    visited[A] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                # 그래프에 노드마다 A의 촌수를 저장.
                result_graph[i] = result_graph[v] + 1
                queue.append(i)
                visited[i] = True


bfs(graph)
if result_graph[B] != 0:
    print(result_graph[B])
else:
    print(-1)