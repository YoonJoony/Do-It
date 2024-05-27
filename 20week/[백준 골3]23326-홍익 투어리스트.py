import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    grid[x][y] = '0'
    count = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                grid[nx][ny] = '0'
                queue.append((nx, ny))
                count += 1
    return count

total_count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':
            total_count += bfs(i, j)

print(total_count)
