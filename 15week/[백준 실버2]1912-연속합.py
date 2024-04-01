n = int(input())
nums = list(map(int, input().split()))

# DP 테이블 초기화: 각 위치에서 끝나는 최대 부분 합을 저장합니다.
dp = [0] * n
dp[0] = nums[0]

# DP 테이블 채우기
for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

# DP 테이블에서 최대 값을 찾아 출력
print(max(dp))
