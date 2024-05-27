from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    distance = [-1] * (N + 1)
    queue = deque([start])
    distance[start] = 0

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if distance[neighbor] == -1:
                queue.append(neighbor)
                distance[neighbor] = distance[v] + 1

    return distance

distance = bfs(1)
max_distance = max(distance)
farthest_barns = [i for i, dist in enumerate(distance) if dist == max_distance]

print(farthest_barns[0], max_distance, len(farthest_barns))
