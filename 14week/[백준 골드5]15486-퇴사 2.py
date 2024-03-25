N = int(input())  # 전체 상담 개수
T = []  # 각 상담을 완료하는데 걸리는 기간
P = []  # 각 상담을 했을 때 받을 수 있는 금액
dp = [0] * (N + 1)  # dp 테이블 초기화

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 뒤에서부터 거꾸로 계산
for i in range(N - 1, -1, -1):
    # 상담이 끝나는 시점이 N을 넘지 않는 경우
    if T[i] + i <= N:
        # i일에 상담을 하는 경우와 하지 않는 경우 중 최대값을 선택
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:  # 상담이 끝나는 시점이 N을 넘는 경우
        dp[i] = dp[i + 1]

print(dp[0])  # 최대 수익 출력
