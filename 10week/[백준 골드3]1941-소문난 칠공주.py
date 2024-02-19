from itertools import combinations
from collections import deque

# 격자판 입력 받기
board = [input() for _ in range(5)]

# 25개의 칸 중 7개를 고르는 모든 조합 생성
candidates = list(combinations(range(25), 7))

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 함수 정의
def bfs(candidate):
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    count_s = 0  # 이다솜파 학생 수

    # 첫 번째 학생을 큐에 넣고 방문 처리
    first = candidate[0]
    q.append(first)
    visited[first // 5][first % 5] = True
    if board[first // 5][first % 5] == 'S':
        count_s += 1

    connected = 1  # 연결된 학생 수
    while q:
        x, y = divmod(q.popleft(), 5)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and (nx * 5 + ny) in candidate:
                visited[nx][ny] = True
                q.append(nx * 5 + ny)
                connected += 1
                if board[nx][ny] == 'S':
                    count_s += 1

    # 연결된 학생 수가 7이고 이다솜파가 4명 이상인지 확인
    return connected == 7 and count_s >= 4


# 가능한 경우의 수 계산
answer = sum(bfs(candidate) for candidate in candidates)
print(answer)
