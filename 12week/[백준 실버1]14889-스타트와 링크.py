import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
graph_origin = [list(map(int, input().split())) for _ in range(N)]
graph = [arr[:] for arr in graph_origin]
member = [_ for _ in range(1, N + 1)]
result = float('inf')
for i in range(N):
    for j in range(N):
        graph[i][j] = graph_origin[i][j] + graph_origin[j][i]

product_team = list(combinations(range(1, N + 1), N // 2))
teamA = []
teamB = []
for i in range(len(product_team) // 2):
    teamA.append(product_team[i])
    teamB.append(product_team[(len(product_team) - 1) - i])


def dfs(n, lst, x, k, team):
    global sm
    if n == 2:
        sm = sm + graph[lst[0]-1][lst[1]-1]
        return

    for i in range(x, N // 2):
        dfs(n + 1, lst + [team[k][i]], i + 1, k, team)


for i in range(len(teamA)):
    sm = 0
    dfs(0, [], 0, i, teamA)
    teamA_S = sm

    sm = 0
    dfs(0, [], 0, i, teamB)
    teamB_S = sm

    if result > (teamA_S - abs(teamB_S)) >= 0:
        result = teamA_S - abs(teamB_S)

    if result > (teamB_S - abs(teamA_S)) >= 0:
        result = teamB_S - abs(teamA_S)


print(result)