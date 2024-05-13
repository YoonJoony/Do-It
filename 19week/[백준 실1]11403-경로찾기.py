from collections import deque
N = int(input())
deq = deque([[] for _ in range(N+1)])

for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for j in range(1, N+1):
        if lst[j-1] == 1:
            deq[i].append(j)

graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N+1):
    queue = deque([deq[i]]) # 인덱스 번호(i)의 노드에 연결된 노드를 queue에 받음.
    visited = [0] * N # 방문 체크
    while queue:
        v = queue.popleft() # 해당 인덱스 번호의 노드가 연결된 노드를 계속 탐색함
        for val in v:
            graph[i-1][val-1] = 1
            if not visited[val-1]: # 탐색하지 않은 노드일 경우
                queue.append(deq[val])
            visited[val-1] = 1     # 탐색한 노드를 방문 체크

for val in graph:
    print(*val)



