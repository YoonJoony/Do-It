# 집의 수 입력 받기
n = int(input())
# 각 집을 빨강, 초록, 파랑으로 칠하는 비용
costs = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(n)]

# 첫 번째 집을 칠하는 비용 초기화
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

# DP 진행
for i in range(1, n):
    # 빨강으로 칠하는 경우
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    # 초록으로 칠하는 경우
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    # 파랑으로 칠하는 경우
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

# 마지막 집까지 칠한 후의 최소 비용 출력
print(min(dp[n-1]))
