import sys
from itertools import product

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
directions = [(0,1), (1,0), (0,-1), (-1,0)]  # 동, 남, 서, 북

# CCTV 위치와 종류를 찾아서 저장
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))

# CCTV가 감시할 수 있는 방향 설정
cctv_dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# 감시 영역을 표시하는 함수
def watch(x, y, direction, temp_office):
    dx, dy = directions[direction]
    while True:
        x += dx
        y += dy
        if x < 0 or x >= n or y < 0 or y >= m or office[x][y] == 6:
            break
        temp_office[x][y] = '#'

# 최소 사각 지대를 계산하는 함수
def get_blind_spot(cctv_seq):
    temp_office = [row[:] for row in office]
    for idx, cctv_dir in enumerate(cctv_seq):
        x, y, cctv_type = cctvs[idx]
        for dir in cctv_dirs[cctv_type][cctv_dir]:
            watch(x, y, dir, temp_office)
    return sum(row.count(0) for row in temp_office)

# 모든 CCTV 방향의 경우의 수에 대해 사각 지대 계산
min_blind_spot = float('inf')
for cctv_seq in product(*[range(len(cctv_dirs[cctv[2]])) for cctv in cctvs]):
    min_blind_spot = min(min_blind_spot, get_blind_spot(cctv_seq))

print(min_blind_spot)
