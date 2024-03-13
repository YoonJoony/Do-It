import sys
from itertools import combinations

input = sys.stdin.readline

# N: 참가 인원 수
N = int(input())
# 각 선수들 간의 시너지(S)를 나타내는 원본 그래프
graph_origin = [list(map(int, input().split())) for _ in range(N)]
# 시너지 점수를 합산하여 저장할 그래프
graph = [arr[:] for arr in graph_origin]
# 참가자 번호 리스트
member = [_ for _ in range(1, N + 1)]
# 최소 차이를 저장할 변수, 무한대로 초기화
result = float('inf')

# graph의 각 요소를 원본 그래프의 i->j와 j->i 시너지 점수의 합으로 업데이트
for i in range(N):
    for j in range(N):
        graph[i][j] = graph_origin[i][j] + graph_origin[j][i]

# 팀 조합 생성
product_team = list(combinations(range(1, N + 1), N // 2))
teamA = []
teamB = []
# 생성된 조합을 반으로 나누어 A팀과 B팀으로 분류
for i in range(len(product_team) // 2):
    teamA.append(product_team[i])
    teamB.append(product_team[(len(product_team) - 1) - i])


# 깊이 우선 탐색(DFS) 함수 정의
def dfs(n, lst, x, k, team):
    global sm
    if n == 2:
        # 두 선수의 시너지 점수 합산
        sm = sm + graph[lst[0]-1][lst[1]-1]
        return

    for i in range(x, N // 2):
        dfs(n + 1, lst + [team[k][i]], i + 1, k, team)


# 각 팀의 시너지 점수 계산 및 최소 차이 업데이트
for i in range(len(teamA)):
    sm = 0
    dfs(0, [], 0, i, teamA)
    teamA_S = sm

    sm = 0
    dfs(0, [], 0, i, teamB)
    teamB_S = sm

    # A팀과 B팀의 시너지 점수 차이 계산 및 result 업데이트
    if result > (teamA_S - abs(teamB_S)) >= 0:
        result = teamA_S - abs(teamB_S)

    if result > (teamB_S - abs(teamA_S)) >= 0:
        result = teamB_S - abs(teamA_S)

# 최소 차이 출력
print(result)
