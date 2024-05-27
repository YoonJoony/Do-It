from collections import deque

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    f1, f2 = map(int, input().split())
    lst[f2].append(f1)


def bfs(lst, n):
    cnt = 0
    visited = [0] * (N + 1)
    visited[n] = 1

    queue = deque([lst[n]])
    while queue:
        v = queue.popleft()
        for val in v:
            if not visited[val]:
                visited[val] = 1
                cnt += 1
                queue.append(lst[val])

    return cnt


max_hacking_computer = []
for i in range(1, N + 1):
    max_hacking_computer.append(bfs(lst, i))

max_hacking = max(max_hacking_computer)
for i in range(1, N+1):
    if max_hacking_computer[i-1] == max_hacking:
        print(i, end=" ")
