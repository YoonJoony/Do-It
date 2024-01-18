import sys
import math
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
graph = [0 for _ in range((math.ceil(K / 10) * 10)+1)]

d = [-1, 1, 2]

print(graph)
def bfs(graph):
    queue = deque([N])
    while queue:
        v = queue.popleft()
        for i in range(3):
            if round(K / 2)

            if md < 0 or md >= len(graph):
                continue

            graph[md] = graph[v] + 1
            queue.append(md)
            print(queue)
            if md == K:
                queue.clear()

while True:
    if N <= round(K / 2):
        N *= 2
    elif N > round(K / 2) or N > K:
        N -= 1
ㅛ


bfs(graph)
print(graph)
print(graph[K])

# 14 26 => 14 13 26
# 14 24 => 14 13 12 24
# 14 23 => 14 13 12 24 23
# 14 22 => 14 13 12 11 22
# 14 21 => 14 13 12 11 22 21
# 14 20 => 14 13 12 11 10 20
# 14 19 => 14 15 16 17 18 19
# 24

# 5 10 20 19 18 17
# 5 10 9 18 17
# 5 6 12 13 14 15 16 17
