from collections import deque

N = int(input())
deq = deque([[] for _ in range(N+1)])
for i in range(1, int(input())+1):
    a, b = map(int, input().split())
    deq[a].append(b)

queue = deque([])
visited = [0] * N
friend = 0

for val in deq[1]:
    if not visited[val-1]:
        friend += 1
        queue.append(deq[val])
    visited[val-1] = 1

for val1 in queue:
    for val2 in val1:
        if not visited[val2-1]:
            friend += 1

print(friend)