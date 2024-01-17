import sys
import math
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
graph = [0 for _ in range(math.ceil(K / 10) * 10)]

print(graph)
d = [-1, 1, 2]


def bfs(graph):
    queue = deque([N])
    while queue:
        v = queue.popleft()
        for i in range(3):
            if d[i] == 2:
                md = v * d[i]
            else:
                md = v + d[i]
            graph[md] = graph[v] + 1
            queue.append(md)
            if graph[md] == K:
                queue.clear()


bfs(graph)
print(graph)

# 33
# 5 10 20 19 18 17
# 5 10 9 18 17
# 5 6 12 13 14 15 16 17
