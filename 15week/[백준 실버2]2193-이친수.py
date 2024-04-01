N = int(input())

# DP 테이블 초기화
DP = [0] * (N+1)

# 초기 조건 설정
DP[1] = 1
if N > 1:
    DP[2] = 1

# 점화식에 따라 DP 테이블 채우기
for i in range(3, N+1):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[N])